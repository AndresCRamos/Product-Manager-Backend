import rest_framework.response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app.token_management import ExpiringTokenAuthentication
from app.permissions import SameZoneOnly, ConveyorOnly, SellerOnly
from .serializers import OrderSerializer, OrderListSerializer, OrderDetailSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = (ExpiringTokenAuthentication, )
    permission_classes = (IsAuthenticated, SameZoneOnly , ConveyorOnly, SellerOnly, )
    queryset = OrderSerializer.Meta.model.objects.all()
    tag = ['order']

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer
