from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Location, MenuItem, Chef
from .forms import MenuItemForm
from django.urls import reverse_lazy


# Location Views
class LocationList(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "menu/location_list.html"


class LocationDetailView(DetailView):
    model = Location
    template_name = "menu/location_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chefs"] = self.object.chefs.filter(is_staff=True)
        context["items"] = self.object.menu_items.all()
        return context


# Menu Item Views
class MenuItemListView(ListView):
    model = MenuItem
    template_name = "menu/menu_item_list.html"
    context_object_name = "items"
    queryset = MenuItem.objects.select_related("chef")


class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "menu/menu_item_create_form.html"
    success_url = reverse_lazy("menu:menu_item_list")


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "menu/menu_item_create_form.html"
    success_url = reverse_lazy("menu:menu_item_list")
