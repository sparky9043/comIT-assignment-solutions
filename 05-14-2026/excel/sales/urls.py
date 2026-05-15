from django.urls import path
from .views import SaleListView, SaleUpdateView, UploadView, RenameColumnView

urlpatterns = [
    path("", UploadView.as_view(), name="upload"),
    path("list/", SaleListView.as_view(), name="sale-list"),
    path("edit/<int:pk>/", SaleUpdateView.as_view(), name="sale-edit"),
    path(
        "rename/<str:internal_name>/", RenameColumnView.as_view(), name="rename-column"
    ),
]
