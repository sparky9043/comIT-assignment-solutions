from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture_1 = models.ImageField(upload_to="products/", blank=True, null=True)
    picture_2 = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name
