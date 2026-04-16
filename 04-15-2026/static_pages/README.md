# Static Pages with Templates and Static Files

## 📌 Description
This project contains 4 static webpages using Django templates and DaisyUI themes for each page.  
The pages are:
1. index (dark)
2. staff (cyberpunk)
3. contact (cupcake)

---

## ⚙️ config/settings.py (modified parts)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'static_pages_templates',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    },
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

## 🌐 config/urls.py

```python
from django.contrib import admin
from django.urls import path
from static_pages_templates import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
]
```

## 🧠 static_pages_templates/views.py

```python

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


```