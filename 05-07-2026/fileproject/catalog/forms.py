from django import forms
from .models import Product
import requests
from django.core.files.base import ContentFile
import os


class ProductForm(forms.ModelForm):
    # Extra URL fields — not model fields, handled manually in save()
    picture_1_url = forms.URLField(required=False, label="Picture 1 — paste a URL")
    picture_2_url = forms.URLField(required=False, label="Picture 2 — paste a URL")

    class Meta:
        model = Product
        fields = ["name", "description", "price", "picture_1", "picture_2"]
        labels = {
            "picture_1": "Picture 1 — upload a file",
            "picture_2": "Picture 2 — upload a file",
        }

    def _download_from_url(self, url):
        """Fetch a remote image and return a ContentFile."""
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        filename = os.path.basename(url.split("?")[0]) or "downloaded_image.jpg"
        return ContentFile(response.content, name=filename)

    def save(self, commit=True):
        instance = super().save(commit=False)

        for field in ("picture_1", "picture_2"):
            url = self.cleaned_data.get(f"{field}_url")
            uploaded_file = self.cleaned_data.get(field)

            if uploaded_file:
                setattr(instance, field, uploaded_file)  # file upload wins
            elif url:
                setattr(instance, field, self._download_from_url(url))

        if commit:
            instance.save()
        return instance
