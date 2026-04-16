from django.urls import path

from . import views

app_name = "static_pages_templates"

urlpatterns = [
    path('', views.index, name="index"),
    path('staff/', views.staff, name="staff"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
]
