from rest_framework.routers import DefaultRouter
from .views import ZoneViewSet

router = DefaultRouter()

router.register(r'zone', ZoneViewSet)

urlpatterns = router.urls
