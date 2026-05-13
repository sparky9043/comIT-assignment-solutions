from rest_framework import viewsets, permissions
from .models import Fruit, Cart, CartItem
from .serializers import FruitSerializer, CartSerializer, CartItemSerializer
from .permissions import IsAdmin, IsAdminOrCustomerReadCart

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


class FruitViewSet(viewsets.ModelViewSet):
    """
    Admins: full CRUD.
    Customers: read-only (list + retrieve).
    """

    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            # Both groups can browse fruits
            return [permissions.IsAuthenticated()]
        # Only admins can create, update, or delete fruits
        return [IsAdmin()]


class CartViewSet(viewsets.ModelViewSet):
    """
    Admins see all carts; customers see only their own.
    """

    serializer_class = CartSerializer
    permission_classes = [IsAdminOrCustomerReadCart]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="admins").exists():
            return Cart.objects.all()
        # Customers access only their own carts
        return Cart.objects.filter(owner=user)

    def perform_create(self, serializer):
        # Cart is always created for the requesting user
        serializer.save(owner=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    """
    Nested under carts; enforces cart ownership for customers.
    """

    serializer_class = CartItemSerializer
    permission_classes = [IsAdminOrCustomerReadCart]

    def get_queryset(self):
        user = self.request.user
        cart_pk = self.kwargs.get("cart_pk")
        qs = CartItem.objects.filter(cart_id=cart_pk)
        if user.groups.filter(name="admins").exists():
            return qs
        # Customers only see items from their own cart
        return qs.filter(cart__owner=user)

    def perform_create(self, serializer):
        user = self.request.user
        cart_pk = self.kwargs.get("cart_pk")

        # Safely fetch the cart or return a clean 404 Not Found
        cart = get_object_or_404(Cart, pk=cart_pk)

        # Prevent customers from adding items to other people's carts
        is_admin = user.groups.filter(name="admins").exists()
        if not is_admin and cart.owner != user:
            raise PermissionDenied(
                "You do not have permission to add items to this cart."
            )

        # If checks pass, save the item to the cart
        serializer.save(cart=cart)
