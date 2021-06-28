import rest_framework.response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import *


class OrderViewSet(ModelViewSet):
    queryset = OrderSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        if self.action in ['retrieve', 'create']:
            return OrderDetailSerializer
        return OrderSerializer



class OrderedProductViewSet(ModelViewSet):
    queryset = OrderedDetailSerializer.Meta.model.objects.all()
    serializer_class = OrderedDetailSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return OrderedDetailSerializer
        return OrderedSerializer
