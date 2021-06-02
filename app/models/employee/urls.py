from django.urls import path
from .views import EmployeeAPIView, EmployeeDetailApiView

urlpatterns = [
    path('', EmployeeAPIView.as_view()),
    path('<int:pk>', EmployeeDetailApiView.as_view())
]
