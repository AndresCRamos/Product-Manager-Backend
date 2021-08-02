from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Purchase, PurchasedProduct
from ..product.serializers import ProductListSerializer, ProductDetailSerializer
from ..supplier.serializers import SupplierSerializer


class PurchasedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedProduct
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        print(validated_data)
        product.quantity -= quantity
        product.save()
        return self.Meta.model.objects.create(**validated_data)


class PurchasedProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedProduct
        exclude = ('purchase', )


class PurchasedProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedProduct
        fields = ('quantity', )

    def validate(self, attrs):
        product = self.context['product']
        quantity = attrs['quantity']
        if quantity+product.quantity > product.max_quantity:
            raise ValidationError(f"exceded max stock {product.max_quantity} of product: { product.pk }, current is "
                                  f"{product.quantity+quantity}")
        return attrs


class PurchasedProductListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance=PurchasedProduct):
        return instance.quantity * instance.product.sale_value

    class Meta:
        model = PurchasedProduct
        exclude = ('id', 'purchase', )


class PurchasedProductDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance=PurchasedProduct):
        return instance.quantity * instance.product.sale_value

    class Meta:
        model = PurchasedProduct
        exclude = ('purchase', )
        read_only_fields = ['id', 'product']


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseCreateSerializer(serializers.ModelSerializer):
    purchased = serializers.ListSerializer(child=PurchasedProductCreateSerializer(), write_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'

    def create(self, validated_data):
        purchased_list = validated_data.pop('purchased')
        purchase = Purchase.objects.create(**validated_data)
        for purchased in purchased_list:
            product = purchased['product']
            PurchasedProduct.objects.create(
                product=product,
                purchase=purchase,
                quantity=purchased['quantity']
            )
        return purchase


class PurchaseListSerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField(method_name='get_supplier', read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'

    def get_supplier(self, obj):
        supplier = obj.supplier
        return {
            'nit': f'{supplier.nit}',
            'name': f'{supplier.name}'
        }

    def to_representation(self, instance):
        data = super(PurchaseListSerializer, self).to_representation(instance)
        purchased_products = PurchasedProductListSerializer.Meta.model.objects.filter(purchase=instance)
        total_price = 0
        for purchased in purchased_products:
            total_price = purchased.quantity * purchased.product.sale_value
        data['total_price'] = total_price
        return data


class PurchaseDetailSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'

    def to_representation(self, instance):
        data = super(PurchaseDetailSerializer, self).to_representation(instance)
        purchased_products = PurchasedProductListSerializer(
            PurchasedProductListSerializer.Meta.model.objects.filter(purchase=instance),
            many=True).data
        total_price = 0
        for product in purchased_products:
            total_price += product['price']
        data['total_price'] = total_price
        data['purchased'] = purchased_products
        return data
