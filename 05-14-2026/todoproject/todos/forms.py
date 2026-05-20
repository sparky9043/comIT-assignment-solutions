from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 rounded-xl border border-gray-200 "
                    "focus:outline-none focus:ring-2 focus:ring-indigo-400 "
                    "bg-white text-gray-800 placeholder-gray-400",
                    "placeholder": "What needs to be done?",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-3 rounded-xl border border-gray-200 "
                    "focus:outline-none focus:ring-2 focus:ring-indigo-400 "
                    "bg-white text-gray-800 placeholder-gray-400",
                    "placeholder": "Add a description (optional)…",
                    "rows": 3,
                }
            ),
        }
