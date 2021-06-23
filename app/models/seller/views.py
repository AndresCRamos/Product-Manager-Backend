from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app.token_management import ExpiringTokenAuthentication
from app.permissions import OwnerOrHROnly, HROnly, OwnSellerOnly
from .serializers import SellerListSerializer, SellerDetailSerializer, SellerSerializer


class SellerViewSet(ModelViewSet):
    authentication_classes = (ExpiringTokenAuthentication, )
    queryset = SellerSerializer.Meta.model.objects.all()
    tag = ['seller']

    def get_serializer_class(self):
        if self.action == 'list':
            return SellerListSerializer
        elif self.action == 'retrieve':
            return SellerDetailSerializer
        return SellerSerializer

    def get_permissions(self):
        print(self.action)
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,  OwnSellerOnly, )
        else:
            self.permission_classes = (IsAuthenticated, HROnly, )
        print(self.permission_classes)
        return super(SellerViewSet, self).get_permissions()
