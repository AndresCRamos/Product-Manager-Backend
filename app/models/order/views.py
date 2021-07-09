from itertools import product

from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import \
    (OrderSerializer, OrderDetailSerializer, OrderListSerializer,
     OrderedProductSerializer, OrderedProductListSerializer, OrderedProductDetailSerializer,
     OrderedProductUpdateSerializer, OrderCreateSerializer
     )


class OrderViewSet(ModelViewSet):
    queryset = OrderSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        if self.action in 'retrieve':
            return OrderDetailSerializer
        if self.action in 'create':
            return OrderCreateSerializer
        return OrderSerializer


class OrderedProductViewSet(ModelViewSet):
    lookup_field = 'product'

    def get_parent(self):
        order_id = self.kwargs['order_pk']
        try:
            return OrderSerializer.Meta.model.objects.get(id=order_id)
        except OrderSerializer.Meta.model.DoesNotExist:
            raise APIException({'detail': "such order doesn't exist"})

    def get_queryset(self):
        order = self.get_parent()
        return OrderedProductDetailSerializer.Meta.model.objects.filter(order=order)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderedProductDetailSerializer
        if self.action == 'list':
            return OrderedProductListSerializer
        if self.action in ['update', 'partial_update']:
            return OrderedProductUpdateSerializer
        return OrderedProductSerializer

    def create(self, request, *args, **kwargs):
        order = self.get_parent()
        data = request.data
        for ordered in data:
            ordered['order'] = order.id
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
