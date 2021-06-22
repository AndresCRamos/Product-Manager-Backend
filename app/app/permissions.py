from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOnly(BasePermission):
    message = 'Must be admin to perform this operation'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.user.type == 'Admin':
                return True
            return False
