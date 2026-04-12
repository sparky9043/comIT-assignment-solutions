from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'car_log/index.html')