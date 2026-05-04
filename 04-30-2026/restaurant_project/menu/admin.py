from django.contrib import admin
from .models import Location, Chef, MenuItem

# Register your models here.

admin.site.register(Location)
admin.site.register(Chef)
admin.site.register(MenuItem)
