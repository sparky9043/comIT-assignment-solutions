from django.db import models
from django.contrib.auth.models import User


class Fruit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    weight_kg = models.DecimalField(max_digits=8, decimal_places=3)  # kg
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)  # currency/kg

    def __str__(self):
        return self.name


class Cart(models.Model):
    # Each customer owns one or more carts
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.pk} — {self.owner.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    fruit = models.ForeignKey(Fruit, on_delete=models.PROTECT)
    quantity_kg = models.DecimalField(
        max_digits=8, decimal_places=3
    )  # how many kg ordered

    @property
    def subtotal(self):
        """Price for this line item: quantity × price per kg."""
        return self.quantity_kg * self.fruit.price_per_kg

    def __str__(self):
        return f"{self.quantity_kg} kg of {self.fruit.name}"
