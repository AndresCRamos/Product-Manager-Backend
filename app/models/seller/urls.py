from rest_framework.routers import DefaultRouter
from .views import SellerViewSet

router = DefaultRouter()

router.register(r'seller', SellerViewSet)
