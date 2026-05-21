from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register_view(request):
    if request.user.is_authenticated:
        return redirect("timers:dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, f"Welcome, {user.username}! Your account has been created."
            )
            return redirect("timers:dashboard")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})
