from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CanceledOrderSerializer, CanceledOrderListSerializer, CanceledOrderDetailSerializer


class CanceledOrderViewSet(ReadOnlyModelViewSet):
    queryset = CanceledOrderSerializer.Meta.model.objects.all()
    serializer_class = CanceledOrderSerializer
    lookup_field = 'order'

    def get_serializer_class(self):
        if self.action == 'list':
            return CanceledOrderListSerializer
        if self.action == 'retrieve':
            return CanceledOrderDetailSerializer
        return CanceledOrderSerializer
