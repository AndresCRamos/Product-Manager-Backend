from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app.token_management import ExpiringTokenAuthentication
from app.permissions import ConveyorOnly
from .serializers import VehicleSerializer, VehicleListSerializer


class VehicleViewSet(ModelViewSet):
    authentication_classes = (ExpiringTokenAuthentication, )
    permission_classes = (ConveyorOnly, )
    queryset = VehicleSerializer.Meta.model.objects.all()
    tag = ['vehicle']

    def get_serializer_class(self):
        if self.action == 'list':
            return VehicleListSerializer
        return VehicleSerializer
