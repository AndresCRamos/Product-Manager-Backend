from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EmployeeSerializer.Meta.model.objects.filter(is_active=True)
    serializer_class = EmployeeSerializer
    tag = ['employee']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data)
        try:
            user = EmployeeSerializer.Meta.model.objects.get(
                id_card=request.data['id_card'],
                email=request.data['email'],
                is_active=False
            )
        except EmployeeSerializer.Meta.model.DoesNotExist:
            return Response(serializer.errors)

        return Response(
            {
                'message': "Inactive user with these data",
                'inactive_user': self.get_serializer(user).data
            }
        )

    def destroy(self, request, pk=None, *args, **kwargs):
        user = self.serializer_class.Meta.model.objects.filter(id_card=pk).first()
        if user:
            user.is_active = False
            user.save()
            return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
        return Response({'error' : 'No such user'}, status=status.HTTP_400_BAD_REQUEST)
