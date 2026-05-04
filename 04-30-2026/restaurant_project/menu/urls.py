from django.urls import path
from .views import (
    LocationList,
    LocationDetailView,
    MenuItemListView,
    MenuItemCreateView,
)

app_name = "menu"

urlpatterns = [
    # Locations
    path("", LocationList.as_view(), name="location_list"),
    path("location/<int:pk>", LocationDetailView.as_view(), name="location_detail"),
    # Menu Items
    path("items/", MenuItemListView.as_view(), name="menu_item_list"),
    path("items/add", MenuItemCreateView.as_view(), name="menu_item_create"),
]
