from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from app.token_management import ExpiringTokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from app.token_management import is_token_expired
from .models import Employee
from .serializers import EmployeeSerializer, LoginSerializer


@permission_classes([AllowAny])
class Login(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None:
            raise AuthenticationFailed('email was not provided')
        if password is None:
            raise AuthenticationFailed('password was not provided')
        try:
            user = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            raise AuthenticationFailed('not user with such email')
        if user:
            pass_valid = check_password(password, user.password)
            if not pass_valid:
                raise AuthenticationFailed('incorrect password')
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                employee = user
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
                            if user.id_card == int(session_data.get('_auth_user_id')):
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
            raise AuthenticationFailed('user isnt active')
        raise AuthenticationFailed('not user with such email')


@permission_classes([IsAuthenticated])
@authentication_classes([ExpiringTokenAuthentication])
class Logout(APIView):
    def get(self, request, *args, **kwargs):
        token_sent = request.META.get('HTTP_AUTHORIZATION').split()[1]
        if token_sent is None:
            return Response(
                {'error': 'no token sent'},
                status=status.HTTP_400_BAD_REQUEST
            )
        token = Token.objects.filter(key=token_sent).first()
        if token:
            user = token.user
            print(user.id_card)
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    if session:
                        session_data = session.get_decoded()
                        print('session id: ', session_data)
                        if user.id_card == int(session_data.get('_auth_user_id')):
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


@permission_classes([AllowAny])
class RefreshToken(APIView):
    def get(self, request, *args, **kwargs):
        old_token = request.META.get('HTTP_AUTHORIZATION')
        if old_token is None:
            return Response({'error': 'no token was provided'}, status=status.HTTP_400_BAD_REQUEST)
        old_token_key = old_token.split()[1]
        try:
            token = Token.objects.get(key=old_token_key)
        except Token.DoesNotExist:
            return Response({'error': 'No such Token'}, status=status.HTTP_400_BAD_REQUEST)
        if token:
            if is_token_expired(token):
                token.delete()
            new_token, created = Token.objects.get_or_create(user=token.user)
            return Response(
                {
                    'token': new_token.key,
                    'refreshed': created
                }
            )
        return Response({'error': 'No such Token'}, status=status.HTTP_400_BAD_REQUEST)
