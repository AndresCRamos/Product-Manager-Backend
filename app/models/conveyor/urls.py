from rest_framework.routers import DefaultRouter
from .views import ConveyorViewSet

router = DefaultRouter()

router.register(r'conveyor', ConveyorViewSet)
