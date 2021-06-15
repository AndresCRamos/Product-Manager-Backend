from rest_framework import serializers
from .models import Product
from ..supplier.serializers import SupplierSerializer


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'min_quantity', 'supplier')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        supplier = instance.supplier
        data.update({
            'supplier_nit': supplier.nit,
            'supplier_name': supplier.name
        })
        return data


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
