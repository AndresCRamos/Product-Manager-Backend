from django.urls import path
from .views import ProductApiView, ProductDetailedAPIView

urlpatterns = [
    path('', ProductApiView.as_view()),
    path('<int:pk>', ProductDetailedAPIView.as_view()),
]
