# showroom/admin.py
from django.contrib import admin
from .models import Branch, Seller, Car

admin.site.register(Branch)
admin.site.register(Seller)
admin.site.register(Car)
