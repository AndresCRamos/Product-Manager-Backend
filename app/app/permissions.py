from rest_framework.permissions import BasePermission, SAFE_METHODS
from models.conveyor.models import Conveyor
from models.seller.models import Seller
from models.order.models import Order


class HROnly(BasePermission):
    message = 'Must be from Human Resources to perform this operation'

    def has_permission(self, request, view):
        if request.user.type in ['HR', 'Admin'] :
            return True
        return False


class ManagerOnly(BasePermission):
    message = 'Must be manager to perform this operation'

    def has_permission(self, request, view):
        return request.user.type in ['Manager', 'Admin']


class OwnerOrHROnly(BasePermission):
    message = 'Must be from human resources, or given employee'

    def has_object_permission(self, request, view, obj):
        if request.user.type in ['HR', 'Admin']:
            return True
        if request.user == obj:
            return True
        return False


class OwnConveyorOnly(BasePermission):
    message = 'Must be from human resources, or given employee'

    def has_object_permission(self, request, view, obj):
        if request.user.type in ['HR', 'Admin']:
            return True
        conveyor = Conveyor.objects.filter(employee=request.user).first()
        if conveyor == obj:
            return True
        return False


class OwnSellerOnly(BasePermission):
    message = 'Must be from human resources, or given employee'

    def has_object_permission(self, request, view, obj):
        if request.user.type in ['HR', 'Admin']:
            return True
        conveyor = Seller.objects.filter(employee=request.user).first()
        if conveyor == obj:
            return True
        return False


class ConveyorOrSellerOnly(BasePermission):
    message = 'Must be conveyor or seller to perform this operation'

    def has_permission(self, request, view):
        if request.user.type in ['Seller', 'Admin', 'Seller']:
            return True
        return False


class SellerOnly(BasePermission):
    message = 'Must be seller to perform this operation'

    def has_permission(self, request, view):
        if request.user.type in ['Seller', 'Admin']:
            return True
        return False


class ConveyorOnly(BasePermission):
    message = 'Must be conveyor to perform this operation'

    def has_permission(self, request, view):
        if request.user.type in ['Conveyor', 'Admin']:
            return True
        return False


class SameZoneOnly(BasePermission):
    message = 'Must be located in the same zone'

    def has_object_permission(self, request, view, obj):
        if not isinstance(obj, (Order, )):
            return False
        zone = obj.client.zone
        if request.user.type == 'Admin':
            return True
        if request.user.type == 'Conveyor':
            conveyor = Conveyor.objects.filter(employee=request.user, zone=zone).first()
            if conveyor:
                return True
        elif request.user.type == 'Seller':
            seller = Seller.objects.filter(employee=request.user, zone=zone).first()
            if seller:
                return True
        return False
