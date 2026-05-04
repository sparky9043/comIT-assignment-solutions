from django.urls import path
from .views import LocationList, LocationDetailView

app_name = "menu"

urlpatterns = [
    path("", LocationList.as_view(), name="location_list"),
    path("location/<int:pk>", LocationDetailView.as_view(), name="location_detail"),
]
