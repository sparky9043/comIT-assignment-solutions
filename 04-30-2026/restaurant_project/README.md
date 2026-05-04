# Homework Assignment: Modified Car App

## CRUD Operations & Search with Class-Based Views

### Restaurant App

I'll using the Car dealership app to create my own version of the app using restaurants

### What Changed
1. I'm using a Restaurant Example using `Location`, `MenuItem`, and `Chef`.
2. Instead of making the "seller" have multiple branches, I made it so that each chef has only one branch
3. Instead of having one "item" per "seller", I updated it so each item can be present in multiple branches
4. I noticed that the `MenuItemInlineDelete` had a bug because it was using `form_valid` instead of `delete`. Since HTMX sends a `DELETE` request instead of using `POST`, I used `delete()` to address this:
```python

class MenuItemInlineDelete(DeleteView):
    model = MenuItem
    success_url = reverse_lazy("menu:location_list")

    # This is where the problem was
    # def form_valid(self):
    #   self.object.delete()
    #   return HttpResponse("")

    # Solution using delete method
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse("")

```
5. Each chef has one location, each menu item has one chef and multiple branches


### Models

```python
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

```

### Things to add or improve in the future
1. Adding Authentication
2. Debug inline-delete when list has only one item left. Currently it doesn't show the `{% empty %}` tag because the page doesn't refresh and the backend and the frontend is decoupled.