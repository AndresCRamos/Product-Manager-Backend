from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet
from .serializers import \
    (PurchaseSerializer, PurchaseDetailSerializer, PurchaseListSerializer,
     PurchasedProductSerializer, PurchasedProductListSerializer, PurchasedProductDetailSerializer,
     PurchasedProductUpdateSerializer, PurchaseCreateSerializer
     )


class PurchaseViewSet(ModelViewSet):
    queryset = PurchaseSerializer.Meta.model.objects.all()
    tag = ['purchase']

    def get_serializer_class(self):
        if self.action == 'list':
            return PurchaseListSerializer
        if self.action in 'retrieve':
            return PurchaseDetailSerializer
        if self.action in 'create':
            return PurchaseCreateSerializer
        return PurchaseSerializer

    @action(methods=['GET'], detail=True, name='Purchase Recieved', url_name='recieved')
    def recieved(self, *args, **kwargs):
        purchase = self.get_object()
        if purchase.status == 'Recieved':
            raise APIException('purchased already recieved')
        purchase.status = 'Recieved'
        purchase.save()
        purchased_list = PurchasedProductListSerializer.Meta.model.objects.filter(purchase=purchase)
        for purchased in purchased_list:
            product = purchased.product
            product.quantity += purchased.quantity
            product.save()
        serializer = PurchaseDetailSerializer(purchase)
        return Response(serializer.data)


class PurchasedProductViewSet(ModelViewSet):
    lookup_field = 'product'
    tag = ['purchase']

    def get_parent(self):
        purchase_id = self.kwargs['purchase_pk']
        try:
            return PurchaseSerializer.Meta.model.objects.get(id=purchase_id)
        except PurchaseSerializer.Meta.model.DoesNotExist:
            raise APIException({'detail': "such Purchase doesn't exist"})

    def get_queryset(self):
        purchase = self.get_parent()
        return PurchasedProductDetailSerializer.Meta.model.objects.filter(purchase=purchase)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PurchasedProductDetailSerializer
        if self.action == 'list':
            return PurchasedProductListSerializer
        if self.action in ['update', 'partial_update']:
            return PurchasedProductUpdateSerializer
        return PurchasedProductSerializer

    def get_serializer_context(self):
        context = super(PurchasedProductViewSet,self).get_serializer_context()
        if self.action in ['update', 'partial_update']:
            context.update({'product': self.get_object().product})
        return context

    def create(self, request, *args, **kwargs):
        purchase = self.get_parent()
        data = request.data
        for purchased in data:
            purchased['purchase'] = purchase.id
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
