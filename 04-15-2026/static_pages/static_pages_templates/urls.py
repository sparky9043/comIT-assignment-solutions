from django.urls import path

from . import views

app_name = "static_pages_templates"

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact")
]
