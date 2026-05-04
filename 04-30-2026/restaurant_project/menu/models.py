from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    open_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.city})"


class Chef(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    location = models.ForeignKey(
        Location,
        related_name="chefs",
        on_delete=models.CASCADE,
    )
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MenuItem(models.Model):
    MENU_ITEM_COURSES = [
        ("appetizer", "appetizer"),
        ("entree", "entrée"),
        ("dessert", "dessert"),
        ("drink", "drink"),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    course = models.CharField(max_length=100, choices=MENU_ITEM_COURSES)
    locations = models.ManyToManyField(
        Location,
        related_name="menu_items",
    )
    chef = models.ForeignKey(
        Chef,
        related_name="menu_items",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.name} ${self.price}"
