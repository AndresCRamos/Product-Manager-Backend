from rest_framework import serializers
from .models import Vehicle


class VehicleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('license_plate', 'model')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
