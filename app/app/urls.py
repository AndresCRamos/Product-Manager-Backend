"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from models.employee import views
from models.client.urls import router as client_router
from models.employee.urls import router as employee_router
from models.product.urls import router as product_router
from models.supplier.urls import router as supplier_router
from models.zone.urls import router as zone_router

schema_view = get_schema_view(
    openapi.Info(
        title='Documentacion',
        default_version='v1',
        description='Product Manager API documentation',
        terms_of_service='',
        contact=openapi.Contact(email='andrecramosr@gmail.com'),
        license=openapi.License(name='BSD')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

models_router = DefaultRouter()
models_router.registry.extend(client_router.registry)
models_router.registry.extend(employee_router.registry)
models_router.registry.extend(product_router.registry)
models_router.registry.extend(supplier_router.registry)
models_router.registry.extend(zone_router.registry)

base_url = [
    path('admin/', admin.site.urls),
]

model_url = [
    path(r'api/v1/', include(models_router.urls))
]

auth_url = [
    path(r'login/', views.Login.as_view()),
    path(r'logout/', views.Logout.as_view()),
    path(r'refresh_token/', views.UserToken.as_view())
]

third_party_url = [
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = base_url + model_url + auth_url + third_party_url
