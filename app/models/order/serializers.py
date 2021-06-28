from rest_framework import serializers
from ..seller.serializers import SellerListSerializer
from ..client.serializers import ClientListSerializer
from ..product.serializers import ProductSerializer
from ..order.models import Order, OrderedProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super(OrderListSerializer, self).to_representation(instance)
        ordered_products = OrderedProductSerializer.Meta.model.objects.filter(order=instance)
        total_price = 0
        for ordered in ordered_products:
            total_price = ordered.quantity * ordered.product.sale_value
        data['total_price'] = total_price
        return data


class OrderedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedProduct
        fields = '__all__'
        read_only_fields = ['order']


class OrderDetailSerializer(serializers.ModelSerializer):
    seller = SellerListSerializer(read_only=True)
    client = ClientListSerializer(read_only=True)
    ordered = serializers.ListSerializer(child=OrderedProductSerializer(), write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        ordered_list = validated_data.pop('ordered')
        order = Order.objects.create(**validated_data)
        for product in ordered_list:
            OrderedProduct.objects.create(
                product=product['product'],
                order=order,
                quantity=product['quantity']
            )
        return order

    def to_representation(self, instance):
        data = super(OrderDetailSerializer, self).to_representation(instance)
        ordered_products = OrderedDetailSerializer(
            OrderedProductSerializer.Meta.model.objects.filter(order=instance),
            many=True).data
        total_price = 0
        for product in ordered_products:
            total_price += product['price']
        data['total_price'] = total_price
        data['ordered'] = ordered_products
        return data


class OrderedDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance=OrderedProduct):
        return instance.quantity * instance.product.sale_value

    class Meta:
        model = OrderedProduct
        exclude = ('order', )
