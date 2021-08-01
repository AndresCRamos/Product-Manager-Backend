from rest_framework import routers
from .views import CanceledOrderViewSet

router = routers.DefaultRouter()

router.register(r'cancelled', CanceledOrderViewSet)
