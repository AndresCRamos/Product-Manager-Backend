from rest_framework import serializers
from .models import Client
from ..zone.serializers import ZoneSerializer


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id_card', 'name', 'last_name', 'telephone', 'cellphone', 'address', 'zone')

    zone = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )


class ClientDetailSerializer(serializers.ModelSerializer):
    zone = ZoneSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ('id_card', 'name', 'last_name', 'telephone', 'cellphone', 'address', 'zone')


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id_card', 'name', 'last_name', 'telephone', 'cellphone', 'address', 'zone')