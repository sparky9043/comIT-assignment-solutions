from django.urls import path
from . import views

app_name = "timers"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # CRUD
    path("timers/create/", views.create_timer, name="create"),
    path("timers/<int:pk>/", views.timer_detail, name="detail"),
    path("timers/<int:pk>/rename/", views.rename_timer, name="rename"),
    path("timers/<int:pk>/delete/", views.delete_timer, name="delete"),
    # Timer controls
    path("timers/<int:pk>/start/", views.start_timer, name="start"),
    path("timers/<int:pk>/stop/", views.stop_timer, name="stop"),
    path("timers/<int:pk>/reset/", views.reset_timer, name="reset"),
    path("timers/<int:pk>/tick/", views.tick_timer, name="tick"),
    # Laps
    path("timers/<int:pk>/lap/", views.add_lap, name="lap"),
]
