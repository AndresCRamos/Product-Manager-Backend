from rest_framework import serializers
from ..canceled_order.models import CanceledOrder
from ..order.serializers import OrderListSerializer, OrderDetailSerializer


class CanceledOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanceledOrder
        fields = '__all__'


class CanceledOrderListSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(read_only=True)

    class Meta:
        model = CanceledOrder
        fields = '__all__'


class CanceledOrderDetailSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer(read_only=True)

    class Meta:
        model = CanceledOrder
        fields = '__all__'
