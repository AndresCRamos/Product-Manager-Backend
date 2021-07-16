from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import DeliverySerializer, DeliveryDetailSerializer,DeliveryListSerializer
from ..order.serializers import OrderSerializer


class DeliveryViewSet(ModelViewSet):
    queryset = DeliverySerializer.Meta.model.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'order'

    def get_serializer_class(self):
        if self.action == 'list':
            return DeliveryListSerializer
        if self.action == 'retrieve':
            return DeliveryDetailSerializer
        return DeliverySerializer

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            order = OrderSerializer.Meta.model.objects.filter(id=request.data['order']).first()
            serializer.save()
            order.state = serializer.data['status']
            order.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)