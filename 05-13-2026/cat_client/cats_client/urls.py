from django.urls import path
from .views import (
    CatListView,
    CatDetailView,
    CatCreateView,
    CatUpdateView,
    CatDeleteView,
)

urlpatterns = [
    path("", CatListView.as_view(), name="cat-list"),
    path("<int:cat_id>/", CatDetailView.as_view(), name="cat-detail"),
    path("new/", CatCreateView.as_view(), name="cat-create"),
    path("<int:cat_id>/edit/", CatUpdateView.as_view(), name="cat-update"),
    path("<int:cat_id>/delete/", CatDeleteView.as_view(), name="cat-delete"),
]
