from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer


class Login(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        try:
            user = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            return Response(
                {'error': 'No user which such email'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if user:
            pass_valid = check_password(password, user.password)
            if not pass_valid:
                return Response(
                    {'error': 'Incorrect password'},
                    status=status.HTTP_400_BAD_REQUEST
                )
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
            return Response(
                {'message': "User isn't active"},
                status=status.HTTP_409_CONFLICT
            )
        return Response(
            {'error': 'No user which such email'},
            status=status.HTTP_400_BAD_REQUEST
        )


class Logout(APIView):
    def get(self, request, *args, **kwargs):
        token_sent = request.GET.get('token')
        if token_sent is None:
            return Response(
                {'error': 'no token sent'},
                status=status.HTTP_400_BAD_REQUEST
            )
        token = Token.objects.filter(key=token_sent).first()
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
