from django import forms
from .models import ColumnLabel


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ColumnRenameForm(forms.ModelForm):
    class Meta:
        model = ColumnLabel
        fields = ["display_name"]
