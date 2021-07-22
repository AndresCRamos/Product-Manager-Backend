from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import DeliverySerializer, DeliveryDetailSerializer, DeliveryListSerializer, DeliveryUpdateSerializer
from ..order.serializers import OrderSerializer


class DeliveryViewSet(ModelViewSet):
    queryset = DeliverySerializer.Meta.model.objects.all()
    lookup_field = 'order'

    def get_serializer_class(self):
        if self.action == 'list':
            return DeliveryListSerializer
        if self.action == 'retrieve':
            return DeliveryDetailSerializer
        if self.action in ['update', 'partial_update']:
            return DeliveryUpdateSerializer
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

    def update(self, request, pk=None, *args, **kwargs):
        partial = self.kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            if 'status' in request.data:
                order = instance.order
                order.state = request.data.get('status')
                order.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        self.kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
