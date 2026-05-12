from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)  # e.g., Persian, Siamese
    age = models.IntegerField()
    weight = models.FloatField()
    vaccinated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
