from django.urls import path
from .views import (
    # Location Views
    LocationList,
    LocationDetailView,
    # Menu Item Views
    MenuItemListView,
    MenuItemCreateView,
    MenuItemUpdateView,
    MenuItemDeleteView,
    MenuItemSearchView,
    # Chef Views
    ChefListView,
)

app_name = "menu"

urlpatterns = [
    # Locations
    path("", LocationList.as_view(), name="location_list"),
    path("location/<int:pk>", LocationDetailView.as_view(), name="location_detail"),
    # Menu Items
    path("items/", MenuItemListView.as_view(), name="menu_item_list"),
    path("items/add", MenuItemCreateView.as_view(), name="menu_item_create"),
    path("items/<int:pk>/edit/", MenuItemUpdateView.as_view(), name="menu_item_update"),
    path(
        "items/<int:pk>/delete/", MenuItemDeleteView.as_view(), name="menu_item_delete"
    ),
    path("items/search", MenuItemSearchView.as_view(), name="menu_item_search"),
    # Chefs
    path("chefs/", ChefListView.as_view(), name="chef_list"),
]
