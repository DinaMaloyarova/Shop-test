from rest_framework.permissions import BasePermission


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user.customer.first()
        if user is None:
            return False
        if user.role == "CLIENT":
            return True
        return False


class OrderCustomerPermission(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user.orders.all()):
            return True
        return False