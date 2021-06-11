from django.urls import path
from .views import EmployeeAPIView, EmployeeDetailApiView

urlpatterns = [
    path('employee/', EmployeeAPIView.as_view()),
    path('employee/<int:pk>', EmployeeDetailApiView.as_view())
]
