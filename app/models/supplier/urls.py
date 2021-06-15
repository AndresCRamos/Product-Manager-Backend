from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet)

urlpatterns = router.urls
