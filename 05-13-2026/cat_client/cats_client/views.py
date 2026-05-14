from django.views import View
from django.shortcuts import render, redirect
from . import services


class CatListView(View):
    """GET /cats/ — list all cats."""

    def get(self, request):
        cats = services.get_all_cats()
        return render(request, "cats_client/cat_list.html", {"cats": cats})


class CatDetailView(View):
    """GET /cats/<id>/ — show a single cat."""

    def get(self, request, cat_id):
        cat = services.get_cat(cat_id)
        return render(request, "cats_client/cat_detail.html", {"cat": cat})


class CatCreateView(View):
    """GET renders the form; POST submits it to the API."""

    def get(self, request):
        return render(request, "cats_client/cat_form.html", {"action": "Create"})

    def post(self, request):
        data = {
            "name": request.POST.get("name"),
            "kind": request.POST.get("kind"),
            "age": int(request.POST.get("age", 0)),
            "weight": float(request.POST.get("weight", 0)),
            "vaccinated": request.POST.get("vaccinated") == "on",
        }
        services.create_cat(data)
        return redirect("cat-list")


class CatUpdateView(View):
    """GET pre-fills the form; PUT sends the update to the API."""

    def get(self, request, cat_id):
        cat = services.get_cat(cat_id)
        return render(
            request, "cats_client/cat_form.html", {"cat": cat, "action": "Update"}
        )

    def post(self, request, cat_id):
        data = {
            "name": request.POST.get("name"),
            "kind": request.POST.get("kind"),
            "age": int(request.POST.get("age", 0)),
            "weight": float(request.POST.get("weight", 0)),
            "vaccinated": request.POST.get("vaccinated") == "on",
        }
        services.update_cat(cat_id, data)
        return redirect("cat-detail", cat_id=cat_id)


class CatDeleteView(View):
    """GET shows a confirmation page; POST performs the deletion."""

    def get(self, request, cat_id):
        cat = services.get_cat(cat_id)
        return render(request, "cats_client/cat_confirm_delete.html", {"cat": cat})

    def post(self, request, cat_id):
        services.delete_cat(cat_id)
        return redirect("cat-list")
