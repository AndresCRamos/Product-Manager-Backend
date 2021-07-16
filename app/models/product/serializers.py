from rest_framework import serializers
from .models import Product
from ..supplier.serializers import SupplierSerializer


class ProductListSerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField('get_supplier', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'min_quantity', 'supplier')

    def get_supplier(self, obj: Product):
        supplier = obj.supplier
        return {
            'nit': supplier.nit,
            'name': supplier.name
        }

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
