from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..client.serializers import ClientListSerializer
from ..order.models import Order, OrderedProduct
from ..product.serializers import ProductListSerializer, ProductDetailSerializer
from ..seller.serializers import SellerListSerializer


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = '__all__'

    def validate(self, attrs):
        product = attrs['product']
        if attrs['quantity'] > product.quantity:
            raise ValidationError(f'not enough stock of product: { product.pk }.')
        return attrs

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        print(validated_data)
        product.quantity -= quantity
        product.save()
        return self.Meta.model.objects.create(**validated_data)


class OrderedProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        exclude = ('order', )


class OrderedProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ('quantity', )


class OrderedProductListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance=OrderedProduct):
        return instance.quantity * instance.product.sale_value

    class Meta:
        model = OrderedProduct
        exclude = ('id', 'order', )


class OrderedProductDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance=OrderedProduct):
        return instance.quantity * instance.product.sale_value

    class Meta:
        model = OrderedProduct
        exclude = ('order', )
        read_only_fields = ['id', 'product']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    ordered = serializers.ListSerializer(child=OrderedProductCreateSerializer(), write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        ordered_list = validated_data.pop('ordered')
        order = Order.objects.create(**validated_data)
        for ordered in ordered_list:
            product = ordered['product']
            OrderedProduct.objects.create(
                product=product,
                order=order,
                quantity=ordered['quantity']
            )
            product.quantity -= ordered['quantity']
            product.save()
        return order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super(OrderListSerializer, self).to_representation(instance)
        ordered_products = OrderedProductListSerializer.Meta.model.objects.filter(order=instance)
        total_price = 0
        for ordered in ordered_products:
            total_price = ordered.quantity * ordered.product.sale_value
        data['total_price'] = total_price
        return data


class OrderDetailSerializer(serializers.ModelSerializer):
    seller = SellerListSerializer(read_only=True)
    client = ClientListSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super(OrderDetailSerializer, self).to_representation(instance)
        ordered_products = OrderedProductListSerializer(
            OrderedProductListSerializer.Meta.model.objects.filter(order=instance),
            many=True).data
        total_price = 0
        for product in ordered_products:
            total_price += product['price']
        data['total_price'] = total_price
        data['ordered'] = ordered_products
        return data
