import rest_framework.response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app.token_management import ExpiringTokenAuthentication
from app.permissions import  HROnly, OwnConveyorOnly
from .serializers import ConveyorSerializer, ConveyorListSerializer, ConveyorDetailSerializer


class ConveyorViewSet(ModelViewSet):
    authentication_classes = (ExpiringTokenAuthentication, )
    queryset = ConveyorSerializer.Meta.model.objects.all()
    tag = ['conveyor']

    def get_serializer_class(self):
        if self.action == 'list':
            return ConveyorListSerializer
        elif self.action == 'retrieve':
            return ConveyorDetailSerializer
        return ConveyorSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,  OwnConveyorOnly, )
        else:
            self.permission_classes = (IsAuthenticated, HROnly, )
        return super(ConveyorViewSet, self).get_permissions()
