from django.urls import path
from .views import LocationList

app_name = "menu"

urlpatterns = [
    path("", LocationList.as_view(), name="location_list"),
]
