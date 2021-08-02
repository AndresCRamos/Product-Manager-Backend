from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import PurchaseViewSet, PurchasedProductViewSet

router = DefaultRouter()
router.register(r'purchase', PurchaseViewSet)

purchased_product_router = NestedSimpleRouter(router, r'purchase', lookup='purchase')
purchased_product_router.register(r'purchased', PurchasedProductViewSet, basename='purchased_product')

