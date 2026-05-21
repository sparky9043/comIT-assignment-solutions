from django.db import models
from django.contrib.auth.models import User


class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timers")
    name = models.CharField(max_length=100, default="My Timer")
    elapsed_seconds = models.PositiveIntegerField(default=0)
    is_running = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def formatted_time(self):
        """Return elapsed seconds as HH:MM:SS string."""
        hours, remainder = divmod(self.elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class Lap(models.Model):
    timer = models.ForeignKey(Timer, on_delete=models.CASCADE, related_name="laps")
    lap_number = models.PositiveIntegerField()
    elapsed_seconds = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["lap_number"]

    def __str__(self):
        return f"Lap {self.lap_number} — {self.timer.name}"

    def formatted_time(self):
        hours, remainder = divmod(self.elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
