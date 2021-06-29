from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import OrderViewSet, OrderedProductViewSet

router = DefaultRouter()
router.register(r'order', OrderViewSet)

ordered_product_router = NestedSimpleRouter(router, r'order', lookup='order')
ordered_product_router.register(r'ordered', OrderedProductViewSet, basename='ordered_product')

