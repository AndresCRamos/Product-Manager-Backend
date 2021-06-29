from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import \
    (OrderSerializer, OrderDetailSerializer, OrderListSerializer,
     OrderedProductSerializer, OrderedProductListSerializer, OrderedProductDetailSerializer)


class OrderViewSet(ModelViewSet):
    queryset = OrderSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        if self.action in ['retrieve', 'create']:
            return OrderDetailSerializer
        return OrderSerializer


class OrderedProductViewSet(ModelViewSet):
    lookup_field = 'product'

    def get_parent(self):
        order_id = self.kwargs['order_pk']
        try:
            return OrderSerializer.Meta.model.objects.get(id=order_id)
        except OrderSerializer.Meta.model.DoesNotExist:
            raise APIException({'error': "such order doesn't exist"})

    def get_queryset(self):
        order = self.get_parent()
        return OrderedProductDetailSerializer.Meta.model.objects.filter(order=order)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderedProductDetailSerializer
        if self.action == 'list':
            return OrderedProductListSerializer
        return OrderedProductSerializer

    def create(self, request, *args, **kwargs):
        order = self.get_parent()
        data = request.data
        for ordered in data:
            ordered['order'] = order.id
            print(ordered)
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
