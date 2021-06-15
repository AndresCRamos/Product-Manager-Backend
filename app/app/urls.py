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
from django.urls import path, include
from models.employee import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('models.client.urls')),
    path('api/v1/', include('models.employee.urls')),
    path('api/v1/', include('models.product.urls')),
    path('api/v1/', include('models.supplier.urls')),
    path('api/v1/', include('models.zone.urls')),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('refresh_token/', views.UserToken.as_view())
]
