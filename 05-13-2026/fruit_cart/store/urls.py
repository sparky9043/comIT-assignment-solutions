# store/urls.py
from rest_framework_nested import routers  # pip install drf-nested-routers
from django.urls import path, include
from .views import FruitViewSet, CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register(r"fruits", FruitViewSet, basename="fruit")
router.register(r"carts", CartViewSet, basename="cart")

# Nested router: /carts/{cart_pk}/items/
carts_router = routers.NestedDefaultRouter(router, r"carts", lookup="cart")
carts_router.register(r"items", CartItemViewSet, basename="cart-items")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(carts_router.urls)),
]
