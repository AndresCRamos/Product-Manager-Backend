from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .authentication_mixins import Authentication
from .serializers import EmployeeSerializer, UserSerializer


class EmployeeAPIView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request):
        employee = self.serializer_class.Meta.model.objects.filter(user__is_active=True)
        serializer = self.serializer_class(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors)


class EmployeeDetailApiView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        employee = self.serializer_class.Meta.model.objects.filter(id_card=pk).first()
        if employee:
            serializer = self.serializer_class(employee)
            return Response(serializer.data)
        return Response({'message' : 'No such user'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = self.serializer_class.Meta.model.objects.filter(user=pk).first()
        serializer = self.serializer_class(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        user_serializer = UserSerializer
        employee = self.serializer_class.Meta.model.objects.filter(id_card=pk).first()
        user = user_serializer.Meta.model.objects.filter(id=employee.user_id).first()
        if user:
            user.is_active = False
            user.save()
            return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
        return Response({'message' : 'No such user'}, status=status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                employee = EmployeeSerializer.Meta.model.objects.filter(user=user.pk).first()
                employee_serializer = EmployeeSerializer(employee)
                if created:
                    return Response(
                        {
                            'token': token.key,
                            'employee': employee_serializer.data,
                            'message': 'Token created'
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    token.delete()
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token = Token.objects.create(user=user)
                    return Response(
                        {
                            'token': token.key,
                            'employee': employee_serializer.data,
                            'message': 'All sessions closed'
                        },
                        status=status.HTTP_201_CREATED
                    )
            return Response(
                {'message': "User isn't active"},
                status=status.HTTP_409_CONFLICT
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class Logout(APIView):
    def get(self, request, *args, **kwargs):
        token_sent = request.GET.get('token')
        print(request.POST)
        print('sent token: ', token_sent)
        token = Token.objects.filter(key=token_sent).first()
        print('token: ', token)
        if token:
            user = token.user
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()
            token.delete()
            session_message = 'User sessions deleted'
            token_message = 'Token deleted'
            return Response(
                {
                    'token_message': token_message,
                    'session_message': session_message
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'no user with this credentials'},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user=UserSerializer.Meta.model.objects.filter(username=username).first()
            )
            return Response(
                {'token': user_token.key}
            )
        except:
            return Response(
                {'error': 'Credentials sent not valid'},
                status=status.HTTP_400_BAD_REQUEST
            )