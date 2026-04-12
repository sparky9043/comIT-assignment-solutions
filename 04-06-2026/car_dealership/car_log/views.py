from django.shortcuts import render

from .models import Car

# Create your views here.
def index(request):
    return render(request, 'car_log/index.html')

def cars(request):
    cars = Car.objects.all()
    context = { 'cars': cars }
    return render(request, 'car_log/cars.html', context)
