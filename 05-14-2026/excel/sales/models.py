from django.db import models
from django.urls import reverse


class Sale(models.Model):
    timestamp = models.DateTimeField()
    product = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    referer = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse("sale-list")


class ColumnLabel(models.Model):
    internal_name = models.CharField(max_length=50, unique=True)  # e.g., 'product'
    display_name = models.CharField(max_length=50)  # e.g., 'Item Name'

    def __str__(self):
        return f"{self.internal_name} -> {self.display_name}"
