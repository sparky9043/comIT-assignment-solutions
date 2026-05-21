from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Timer, Lap
from django.db.models import F

# ─── Dashboard ──────────────────────────────────────────────────────────────


@login_required
def dashboard(request):
    timers = Timer.objects.filter(user=request.user).prefetch_related("laps")
    return render(request, "timers/dashboard.html", {"timers": timers})


# ─── Create ─────────────────────────────────────────────────────────────────


@login_required
@require_http_methods(["POST"])
def create_timer(request):
    name = request.POST.get("name", "My Timer").strip() or "My Timer"
    timer = Timer.objects.create(user=request.user, name=name)
    # Return just the new timer card via HTMX
    return render(request, "timers/partials/timer_card.html", {"timer": timer})


# ─── Read (single card refresh) ──────────────────────────────────────────────


@login_required
def timer_detail(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    return render(request, "timers/partials/timer_card.html", {"timer": timer})


# ─── Update — Rename ─────────────────────────────────────────────────────────


@login_required
@require_http_methods(["POST"])
def rename_timer(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    new_name = request.POST.get("name", "").strip()
    if new_name:
        timer.name = new_name
        timer.save()
    return render(request, "timers/partials/timer_card.html", {"timer": timer})


# ─── Update — Tick (called by client every second while running) ──────────────


@login_required
@require_http_methods(["POST"])
def tick_timer(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    if timer.is_running:
        # F() expression prevents race conditions by incrementing atomically directly in the DB
        Timer.objects.filter(pk=pk).update(elapsed_seconds=F("elapsed_seconds") + 1)
        timer.refresh_from_db()
    return render(request, "timers/partials/timer_display.html", {"timer": timer})


# ─── Update — Start ───────────────────────────────────────────────────────────
@login_required
@require_http_methods(["POST"])
def start_timer(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    timer.is_running = True
    timer.save(update_fields=["is_running", "updated_at"])  # Only update state
    return render(request, "timers/partials/timer_card.html", {"timer": timer})


# ─── Update — Stop ────────────────────────────────────────────────────────────
@login_required
@require_http_methods(["POST"])
def stop_timer(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    timer.is_running = False
    timer.save(
        update_fields=["is_running", "updated_at"]
    )  # Don't overwrite elapsed_seconds
    return render(request, "timers/partials/timer_card.html", {"timer": timer})


# ─── Update — Reset ───────────────────────────────────────────────────────────


@login_required
@require_http_methods(["POST"])
def reset_timer(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    timer.is_running = False
    timer.elapsed_seconds = 0
    timer.save()
    timer.laps.all().delete()
    return render(request, "timers/partials/timer_card.html", {"timer": timer})


# ─── Create Lap ──────────────────────────────────────────────────────────────


@login_required
@require_http_methods(["POST"])
def add_lap(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    lap_number = timer.laps.count() + 1
    Lap.objects.create(
        timer=timer,
        lap_number=lap_number,
        elapsed_seconds=timer.elapsed_seconds,
    )
    return render(request, "timers/partials/lap_list.html", {"timer": timer})


# ─── Delete Timer ─────────────────────────────────────────────────────────────


@login_required
@require_http_methods(["DELETE"])
def delete_timer(request, pk):
    timer = get_object_or_404(Timer, pk=pk, user=request.user)
    timer.delete()
    # Return empty response — HTMX will remove the element
    return HttpResponse(status=200)
