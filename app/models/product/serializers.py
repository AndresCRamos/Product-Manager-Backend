from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('no_VAT_value', 'min_quantity', 'max_quantity')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'purchase_value': instance.purchase_value,
            'sale_value': instance.sale_value,
            'supplier_nit': instance.supplier.nit,
            'supplier_name': instance.supplier.name
        }


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'sale_value': instance.sale_value,
            'no_VAT_value': instance.no_VAT_value,
            'purchase_value': instance.purchase_value,
            'min_quantity': instance.min_quantity,
            'max_quantity': instance.max_quantity,
            'supplier_id': instance.supplier.id,
            'supplier_nit': instance.supplier.nit,
            'supplier_name': instance.supplier.name
        }

