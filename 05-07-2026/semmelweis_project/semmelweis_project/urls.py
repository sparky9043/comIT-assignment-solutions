# semmelweis_project/urls.py
# The root URLconf: includes the analysis app's urls under the empty prefix (""),
# meaning all analysis URLs are available at the site root.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # namespace="analysis" means URL names are referenced as "analysis:dashboard" etc.
    path("", include("analysis.urls", namespace="analysis")),
    # In development, Django serves media files (uploaded images) itself.
    # static() returns an empty list in production when DEBUG=False.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
