from rest_framework import serializers
from .models import Product, ProductSupplier


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSupplier
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
