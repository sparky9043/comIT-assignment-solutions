from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("product/add/", views.ProductCreateView.as_view(), name="create"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="update"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
]
