from rest_framework import serializers
from .models import Seller
from ..employee.serializers import EmployeeListSerializer, EmployeeSerializer
from ..zone.serializers import ZoneSerializer


class SellerListSerializer(serializers.ModelSerializer):
    employee = EmployeeListSerializer(read_only=True)
    zone = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Seller
        fields = '__all__'


class SellerDetailSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)
    zone = ZoneSerializer(required=True)

    class Meta:
        model = Seller
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
