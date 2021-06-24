from rest_framework import serializers
from .models import Order
from ..seller.serializers import SellerSerializer
from ..client.serializers import ClientSerializer


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_date', 'delivery_date', 'state', 'client')


class OrderDetailSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
