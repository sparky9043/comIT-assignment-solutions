# client_app/urls.py
from django.urls import path, include

urlpatterns = [
    path("", include("store.urls")),
]
