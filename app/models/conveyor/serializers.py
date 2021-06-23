from rest_framework import serializers
from .models import Conveyor
from ..employee.serializers import EmployeeListSerializer, EmployeeSerializer
from ..zone.serializers import ZoneSerializer


class ConveyorListSerializer(serializers.ModelSerializer):
    employee = EmployeeListSerializer(read_only=True)
    zone = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Conveyor
        fields = '__all__'


class ConveyorDetailSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)
    zone = ZoneSerializer(required=True)

    class Meta:
        model = Conveyor
        fields = '__all__'


class ConveyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conveyor
        fields = '__all__'
