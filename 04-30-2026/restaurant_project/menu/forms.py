from django import forms
from .models import Chef, MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "price", "course", "locations", "chef"]


class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ["first_name", "last_name", "dob", "location", "is_staff"]
