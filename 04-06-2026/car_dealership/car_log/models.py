from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=75)
    gear = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
