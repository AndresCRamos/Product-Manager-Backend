from django.urls import path
from .views import SupplierAPIView, SupplierDetailedAPIView

urlpatterns = [
    path('', SupplierAPIView.as_view()),
    path('<int:pk>', SupplierDetailedAPIView.as_view())
]