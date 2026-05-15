# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # Admin – Fruits
    path("admin-dash/", views.admin_fruits, name="admin-dash"),
    path("admin/fruits/create/", views.admin_fruit_create, name="admin-fruit-create"),
    path(
        "admin/fruits/<int:pk>/edit/", views.admin_fruit_edit, name="admin-fruit-edit"
    ),
    path(
        "admin/fruits/<int:pk>/delete/",
        views.admin_fruit_delete,
        name="admin-fruit-delete",
    ),
    # Admin – Carts
    path("admin/carts/", views.admin_carts, name="admin-carts"),
    path("admin/carts/create/", views.admin_cart_create, name="admin-cart-create"),
    path(
        "admin/carts/<int:pk>/delete/",
        views.admin_cart_delete,
        name="admin-cart-delete",
    ),
    path(
        "admin/carts/<int:cart_pk>/items/add/",
        views.admin_item_add,
        name="admin-item-add",
    ),
    path(
        "admin/carts/<int:cart_pk>/items/<int:item_pk>/update/",
        views.admin_item_update,
        name="admin-item-update",
    ),
    path(
        "admin/carts/<int:cart_pk>/items/<int:item_pk>/delete/",
        views.admin_item_delete,
        name="admin-item-delete",
    ),
    # Customer
    path("customer-dash/", views.customer_dashboard, name="customer-dash"),
    path(
        "customer/carts/create/",
        views.customer_cart_create,
        name="customer-cart-create",
    ),
    path(
        "customer/carts/<int:pk>/delete/",
        views.customer_cart_delete,
        name="customer-cart-delete",
    ),
    path(
        "customer/carts/<int:cart_pk>/items/add/",
        views.customer_item_add,
        name="customer-item-add",
    ),
    path(
        "customer/carts/<int:cart_pk>/items/<int:item_pk>/update/",
        views.customer_item_update,
        name="customer-item-update",
    ),
    path(
        "customer/carts/<int:cart_pk>/items/<int:item_pk>/delete/",
        views.customer_item_delete,
        name="customer-item-delete",
    ),
]
