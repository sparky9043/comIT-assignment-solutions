from django.urls import path
from .views import (
    IndexView,
    PostListView,
    PostCreateView,
    PostEditView,
    PostUpdateView,
    PostDeleteView,
    PostSearchView,
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
)

urlpatterns = [
    # Auth
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    # Blog
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("posts/search/", PostSearchView.as_view(), name="post_search"),
    path("posts/<int:pk>/edit/", PostEditView.as_view(), name="post_edit"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
