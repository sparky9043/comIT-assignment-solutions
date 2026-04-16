from django.shortcuts import render

# Create your views here.

app_name = "static_pages_templates"

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'static_pages_templates/home.html', ctx)

def contact(request):
    return render(request, 'static_pages_templates/contact.html')
