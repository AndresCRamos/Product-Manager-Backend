from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderedProductViewSet

router = DefaultRouter()

router.register(r'order', OrderViewSet)
router.register(r'ordered', OrderedProductViewSet)
