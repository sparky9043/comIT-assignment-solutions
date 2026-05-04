from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Location

# Create your views here.


class LocationList(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "menu/location_list.html"


class LocationDetailView(DetailView):
    model = Location
    template_name = "menu/location_detail.html"
