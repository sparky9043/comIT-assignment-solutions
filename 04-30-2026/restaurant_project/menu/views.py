from django.shortcuts import render
from django.views.generic import ListView
from .models import Location

# Create your views here.


class LocationList(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "menu/location_list.html"
