# showroom/forms.py
from django import forms
from .models import Car, Seller


class CarForm(forms.ModelForm):
    class Meta:
        model  = Car
        fields = ['make', 'model', 'year', 'price',
                  'transmission', 'branch', 'seller']


class SellerForm(forms.ModelForm):
    class Meta:
        model  = Seller
        fields = ['first_name', 'last_name', 'branches', 'is_active']