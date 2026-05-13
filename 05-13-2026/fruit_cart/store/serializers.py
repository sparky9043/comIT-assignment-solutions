from rest_framework import serializers
from .models import Fruit, Cart, CartItem


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ["id", "name", "weight_kg", "price_per_kg"]


class CartItemSerializer(serializers.ModelSerializer):
    fruit_name = serializers.ReadOnlyField(source="fruit.name")
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "fruit", "fruit_name", "quantity_kg", "subtotal"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "owner", "created_at", "items", "total"]
        read_only_fields = ["owner", "created_at"]

    def get_total(self, obj):
        """Sum of all item subtotals in the cart."""
        return sum(item.subtotal for item in obj.items.all())
