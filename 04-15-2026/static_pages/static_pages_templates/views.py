from django.shortcuts import render

# Create your views here.

app_name = "static_pages_templates"

def index(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'static_pages_templates/index.html', ctx)

def staff(request):
    return render(request, 'static_pages_templates/staff.html')

def contact(request):
    return render(request, 'static_pages_templates/contact.html')
