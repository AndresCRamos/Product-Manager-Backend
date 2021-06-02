from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(APIView):
    def get(self, request):
        employee = Employee.objects.filter(user__is_active=True)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors)


class EmployeeDetailApiView(APIView):
    def get(self, request, pk):
        employee = Employee.objects.filter(id_card=pk).first()
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        return Response({'message' : 'No such user'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = Employee.objects.filter(user=pk).first()
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        employee = Employee.objects.filter(id_card=pk).first()
        user = User.objects.filter(id=employee.user_id).first()
        if user:
            user.is_active = False
            user.save()
        return Response({'message' : 'No such user'}, status=status.HTTP_400_BAD_REQUEST)

