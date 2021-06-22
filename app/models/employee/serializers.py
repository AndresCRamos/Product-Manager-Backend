from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id_card', 'email', 'first_name', 'last_name', 'cellphone', 'city', 'neighborhood',
            'address', 'type'
        )
        type = serializers.ChoiceField(choices=Employee.EmployeeType.choices)

    def create(self, validated_data):
        password = validated_data['password1']
        if validated_data['password1'] == validated_data['password2']:
            del validated_data["password1"]
            del validated_data["password2"]
        user = super(EmployeeSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user
