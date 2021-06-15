from rest_framework import status
from rest_framework.views import Response, APIView
from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    queryset = SupplierSerializer.Meta.model.objects.all()
    serializer_class = SupplierSerializer
