from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Location, MenuItem, Chef
from .forms import MenuItemForm, ChefForm
from django.urls import reverse_lazy
from django.db.models import Q


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


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "menu/menu_item_delete.html"
    success_url = reverse_lazy("menu:menu_item_list")


class MenuItemSearchView(ListView):
    model = MenuItem
    template_name = "menu/partials/menu_item_table.html"
    context_object_name = "items"

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        qs = MenuItem.objects.select_related("chef")
        if q:
            qs = qs.filter(
                Q(name__icontains=q)
                | Q(chef__last_name__icontains=q)
                | Q(chef__first_name__icontains=q)
                | Q(locations__name__icontains=q)
            )

        return qs


# Chef Views
class ChefListView(ListView):
    model = Chef
    template_name = "menu/chef_list.html"
    context_object_name = "chefs"
    queryset = Chef.objects.select_related("location")


class ChefDetailView(DetailView):
    model = Chef
    template_name = "menu/chef_detail.html"
    context_object_name = "chef"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = self.object.menu_items.prefetch_related("locations")
        context["items"] = items
        return context


class ChefCreateView(CreateView):
    model = Chef
    form_class = ChefForm
    template_name = "menu/chef_create_form.html"
    success_url = reverse_lazy("menu:chef_list")


class ChefUpdateView(UpdateView):
    model = Chef
    form_class = ChefForm
    template_name = "menu/chef_create_form.html"
    success_url = reverse_lazy("menu:chef_list")


class ChefDeleteView(DeleteView):
    model = Chef
    template_name = "menu/chef_delete.html"
    success_url = reverse_lazy("menu:chef_list")
