import pandas as pd
from django.views.generic import ListView, UpdateView, FormView, View
from django.db.models import Sum, Q
from django.db.models.functions import ExtractMonth, ExtractYear
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Sale, ColumnLabel
from .forms import UploadFileForm
from django.db import models


class SaleListView(ListView):
    model = Sale
    template_name = "sales/sale_list.html"
    context_object_name = "sales"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(
                Q(product__icontains=search_query)
                | Q(customer_name__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Summary Calculation: Group by Year and Month
        context["summary"] = (
            Sale.objects.annotate(
                year=ExtractYear("timestamp"), month=ExtractMonth("timestamp")
            )
            .values("year", "month")
            .annotate(total_revenue=Sum("revenue"), count=models.Count("id"))
            .order_by("-year", "-month")
        )

        # Get Column Labels
        labels = ColumnLabel.objects.all()
        context["labels"] = {l.internal_name: l.display_name for l in labels}
        return context


class SaleUpdateView(UpdateView):
    model = Sale
    fields = "__all__"
    template_name = "sales/sale_form.html"
    success_url = reverse_lazy("sale-list")


class UploadView(FormView):
    template_name = "sales/upload.html"
    form_class = UploadFileForm
    success_url = reverse_lazy("sale-list")

    def form_valid(self, form):
        file = self.request.FILES["file"]
        df = pd.read_excel(file)

        # Clean Revenue string (€34.99 -> 34.99)
        if df["Revenue"].dtype == "O":
            df["Revenue"] = df["Revenue"].replace("[€,]", "", regex=True).astype(float)

        sales_instances = []
        for _, row in df.iterrows():
            sales_instances.append(
                Sale(
                    timestamp=row["Timestamp"],
                    product=row["Product"],
                    revenue=row["Revenue"],
                    referer=row["Referer"],
                    customer_name=row["Customer name"],
                    country=row["Country"],
                    email=row["Email"],
                )
            )
        Sale.objects.bulk_create(sales_instances)

        # Initialize default labels if they don't exist
        columns = [
            "timestamp",
            "product",
            "revenue",
            "referer",
            "customer_name",
            "country",
            "email",
        ]
        for col in columns:
            ColumnLabel.objects.get_or_create(
                internal_name=col,
                defaults={"display_name": col.replace("_", " ").title()},
            )

        return super().form_valid(form)


class RenameColumnView(UpdateView):
    model = ColumnLabel
    fields = ["display_name"]
    template_name = "sales/rename_column.html"
    success_url = reverse_lazy("sale-list")

    def get_object(self):
        return ColumnLabel.objects.get(internal_name=self.kwargs["internal_name"])
