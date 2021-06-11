from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

    def create(self, validated_data):
        password = validated_data['password1']
        if validated_data['password1'] == validated_data['password2']:
            del validated_data["password1"]
            del validated_data["password2"]
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = ('user', 'id_card', 'cellphone', 'city', 'neighborhood', 'address', 'type')

    def create(self, validated_data):
        id_card = validated_data.pop('id_card')
        cellphone = validated_data.pop('cellphone')
        city = validated_data.pop('city')
        neighborhood = validated_data.pop('neighborhood')
        address = validated_data.pop('address')
        employee_type = validated_data.pop('type')
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        employee, created = Employee.objects.update_or_create(
            user=user,
            id_card=id_card,
            cellphone=cellphone,
            city=city,
            neighborhood=neighborhood,
            address=address,
            type=employee_type
        )
        return employee
