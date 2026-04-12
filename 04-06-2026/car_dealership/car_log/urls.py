from django.urls import path

from . import views

app_name = "car_log"

urlpatterns = [
    path('', views.index, name="index")
]
