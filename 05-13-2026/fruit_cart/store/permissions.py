from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """Full access for users in the 'admins' group."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="admins").exists()


class IsCustomer(BasePermission):
    """Customers can only touch carts/items — not fruits."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="customers").exists()


class IsAdminOrCustomerReadCart(BasePermission):
    """
    Admins: unrestricted.
    Customers: full CRUD on carts, read-only on fruits.
    """

    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name="admins").exists():
            return True
        if user.groups.filter(name="customers").exists():
            # Customers are blocked at the view level for fruit writes;
            # this permission just gates the cart/item views.
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Customers may only access their own carts."""
        from .models import Cart, CartItem

        if request.user.groups.filter(name="admins").exists():
            return True
        if isinstance(obj, Cart):
            return obj.owner == request.user
        if isinstance(obj, CartItem):
            return obj.cart.owner == request.user
        return False
