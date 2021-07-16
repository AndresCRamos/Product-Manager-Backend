from rest_framework import routers
from .views import DeliveryViewSet

router = routers.DefaultRouter()

router.register(r'delivery', DeliveryViewSet)
