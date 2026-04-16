from django.shortcuts import render

# Create your views here.
from .models import Department, Staff

app_name = "static_pages_templates"

def index(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'static_pages_templates/index.html', ctx)

def staff(request):
    staff = Staff.objects.all()
    context = { 'staff': staff }
    return render(request, 'static_pages_templates/staff.html', context)

def contact(request):
    return render(request, 'static_pages_templates/contact.html')
