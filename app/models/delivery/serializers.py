from rest_framework import serializers
from .models import Delivery
from ..order.serializers import OrderListSerializer, OrderDetailSerializer
from ..conveyor.serializers import ConveyorListSerializer
from ..vehicle.serializers import VehicleListSerializer


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryListSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(read_only=True)
    conveyor = serializers.SerializerMethodField('get_employee', read_only=True)
    vehicle = VehicleListSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'

    def get_employee(self, obj):
        conveyor = obj.conveyor
        return {
            'employee': {
                'name': f'{conveyor.employee.first_name} {conveyor.employee.last_name}',
                'email': f'{conveyor.employee.email}'
            },
            'zone': conveyor.zone.name
        }


class DeliveryDetailSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer(read_only=True)
    conveyor = ConveyorListSerializer(read_only=True)
    vehicle = VehicleListSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        exclude = ('order', 'id')
