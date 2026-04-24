from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    RedirectView,
)
from django.views.generic.dates import (
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    WeekArchiveView,
    DayArchiveView,
    TodayArchiveView,
    DateDetailView,
)

from .models import Animal
from .forms import AnimalSearchForm


# ---------------------------------------------------------------------------
# RedirectView — /zoo/ redirects to the home page
# ---------------------------------------------------------------------------
class ZooRedirectView(RedirectView):
    """
    RedirectView issues an HTTP redirect without rendering any template.
    'permanent=False' sends a 302 (temporary) redirect.
    'pattern_name' resolves the destination by named URL instead of a
    hard-coded string, so it stays correct if the URL ever changes.
    """

    permanent = False
    pattern_name = "animals:home"


# ---------------------------------------------------------------------------
# TemplateView — Home / landing page
# ---------------------------------------------------------------------------
class HomeView(TemplateView):
    """
    TemplateView renders a fixed template with no model involved.
    We override get_context_data() to inject extra variables:
      - page_title: used in the <title> tag and heading
      - total_animals: total count of animals in the zoo
      - captive_count: how many were born in captivity
      - wild_count: how many were born in the wild
    """

    template_name = "animals/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Welcome to the Zoo"
        context["total_animals"] = Animal.objects.count()
        context["captive_count"] = Animal.objects.filter(born_in_captivity=True).count()
        context["wild_count"] = Animal.objects.filter(born_in_captivity=False).count()
        return context


# ---------------------------------------------------------------------------
# ListView — All animals
# ---------------------------------------------------------------------------
class AnimalListView(ListView):
    """
    ListView queries all Animal objects and passes them to the template.
    context_object_name renames the default 'object_list' to 'animals'.
    paginate_by splits results into pages; Django automatically provides
    the 'page_obj' and 'paginator' variables for building pagination links.

    Extra context added:
      - page_title: for the browser tab and heading
      - total_count: total number of animals across all pages
    """

    model = Animal
    template_name = "animals/animal_list.html"
    context_object_name = "animals"
    paginate_by = 5

    def get_queryset(self):
        return Animal.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Animals"
        context["total_count"] = Animal.objects.count()
        return context


# ---------------------------------------------------------------------------
# DetailView — Single animal
# ---------------------------------------------------------------------------
class AnimalDetailView(DetailView):
    """
    DetailView looks up a single Animal by its pk (from the URL) and
    passes it to the template as 'animal' (context_object_name).

    Extra context added:
      - page_title: uses the animal's name
      - is_elderly: True if the animal is over 15 years old
      - weight_category: a human-readable size label derived from weight
    """

    model = Animal
    template_name = "animals/animal_detail.html"
    context_object_name = "animal"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        animal = self.get_object()
        context["page_title"] = f"Animal: {animal.name}"
        context["is_elderly"] = animal.age > 15
        context["weight_category"] = self._weight_category(animal.weight)
        return context

    @staticmethod
    def _weight_category(weight):
        """Returns a human-readable weight category label."""
        if weight < 10:
            return "Small"
        elif weight < 100:
            return "Medium"
        elif weight < 500:
            return "Large"
        return "Very Large"


# ---------------------------------------------------------------------------
# CreateView — Add a new animal
# ---------------------------------------------------------------------------
class AnimalCreateView(CreateView):
    """
    CreateView displays a blank ModelForm for Animal, validates it on POST,
    and saves a new instance. After saving it redirects to the URL returned
    by Animal.get_absolute_url() (no success_url needed when that is defined).

    Extra context added:
      - page_title: shown in the heading
      - form_action: tells the shared template this is a Create operation
    """

    model = Animal
    fields = ["name", "age", "weight", "born_in_captivity", "date_added"]
    template_name = "animals/animal_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add New Animal"
        context["form_action"] = "Create"
        return context


# ---------------------------------------------------------------------------
# UpdateView — Edit an existing animal
# ---------------------------------------------------------------------------
class AnimalUpdateView(UpdateView):
    """
    UpdateView is identical to CreateView but pre-fills the form with the
    existing Animal data (looked up by pk from the URL).

    Extra context added:
      - page_title: includes the animal's current name
      - form_action: tells the shared template this is an Update operation
    """

    model = Animal
    fields = ["name", "age", "weight", "born_in_captivity", "date_added"]
    template_name = "animals/animal_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"Edit: {self.object.name}"
        context["form_action"] = "Update"
        return context


# ---------------------------------------------------------------------------
# DeleteView — Delete an animal
# ---------------------------------------------------------------------------
class AnimalDeleteView(DeleteView):
    """
    DeleteView shows a confirmation page on GET, then deletes the object
    and redirects to success_url on POST.

    reverse_lazy() is used instead of reverse() because Python evaluates
    class bodies at import time — before the URL configuration is loaded.

    Extra context added:
      - page_title: warns the user which animal they are about to delete
    """

    model = Animal
    template_name = "animals/animal_confirm_delete.html"
    success_url = reverse_lazy("animals:animal-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"Delete: {self.object.name}"
        return context


# ---------------------------------------------------------------------------
# FormView — Search animals
# ---------------------------------------------------------------------------
class AnimalSearchView(FormView):
    """
    FormView for searching animals. Uses GET so results are bookmarkable
    and no CSRF token is needed.

    The key challenge: FormView only binds form data on POST by default.
    We override get_form_kwargs() to also bind GET params, which makes the
    form validate when the user submits the search via GET.

    All search logic lives in get_context_data() so it runs on every request.

    Extra context added:
      - page_title: describes the page
      - results: the QuerySet of matching animals (after form submission)
      - result_count: number of matches
      - search_performed: boolean flag so the template knows to show results
    """

    template_name = "animals/animal_search.html"
    form_class = AnimalSearchForm

    def get_form_kwargs(self):
        """
        By default, FormView only binds form data on POST.
        This override also binds GET params so the form validates on GET.
        Without this, the form is always unbound on GET and is_valid()
        never returns True, so no search ever runs.
        """
        kwargs = super().get_form_kwargs()
        if self.request.method == "GET" and self.request.GET:
            kwargs["data"] = self.request.GET
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Search Animals"
        context["results"] = None
        context["search_performed"] = False

        form = context["form"]
        # Only run the search if GET params are present and the form is valid
        if self.request.GET and form.is_valid():
            data = form.cleaned_data
            queryset = Animal.objects.all()

            # Filter by name (case-insensitive partial match)
            if data.get("name"):
                queryset = queryset.filter(name__icontains=data["name"])

            # Filter by age range
            if data.get("min_age") is not None:
                queryset = queryset.filter(age__gte=data["min_age"])
            if data.get("max_age") is not None:
                queryset = queryset.filter(age__lte=data["max_age"])

            # Filter by weight range
            if data.get("min_weight") is not None:
                queryset = queryset.filter(weight__gte=data["min_weight"])
            if data.get("max_weight") is not None:
                queryset = queryset.filter(weight__lte=data["max_weight"])

            # Filter by born_in_captivity
            if data.get("born_in_captivity") is not None:
                queryset = queryset.filter(born_in_captivity=data["born_in_captivity"])

            context["results"] = queryset
            context["result_count"] = queryset.count()
            context["search_performed"] = True

        return context


# ---------------------------------------------------------------------------
# ArchiveIndexView — All years that have animals
# ---------------------------------------------------------------------------
class AnimalArchiveIndexView(ArchiveIndexView):
    """
    ArchiveIndexView groups all objects by the date_field and provides
    'date_list' in the context: a queryset of distinct years that have
    at least one record. allow_empty=True returns an empty page instead
    of a 404 when no animals exist yet.

    Extra context added:
      - page_title
      - total_years: how many distinct years have animals
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_archive.html"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Animal Archive"
        context["total_years"] = len(context.get("date_list") or [])
        return context


# ---------------------------------------------------------------------------
# YearArchiveView — Animals added in a specific year
# ---------------------------------------------------------------------------
class AnimalYearArchiveView(YearArchiveView):
    """
    YearArchiveView filters objects whose date_field falls in the given year,
    captured from the URL (e.g. /archive/2024/).
    make_object_list=True puts the actual Animal objects (not just month
    dates) into 'object_list' so we can display them in the template.

    Extra context added:
      - page_title: includes the year
      - animal_count: number of animals added that year
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_archive_year.html"
    make_object_list = True
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"Animals Added in {self.get_year()}"
        context["animal_count"] = len(context.get("object_list") or [])
        return context


# ---------------------------------------------------------------------------
# MonthArchiveView — Animals added in a specific month
# ---------------------------------------------------------------------------
class AnimalMonthArchiveView(MonthArchiveView):
    """
    MonthArchiveView filters by year + month from the URL (e.g. /archive/2024/3/).
    month_format='%m' allows numeric months instead of the default '%b' (Jan).

    Extra context added:
      - page_title: includes the month name and year
      - animal_count: number of animals added that month
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_archive_month.html"
    month_format = "%m"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month_name = context["month"].strftime("%B")  # e.g. "March"
        context["page_title"] = f"Animals Added in {month_name} {self.get_year()}"
        context["animal_count"] = context["object_list"].count()
        return context


# ---------------------------------------------------------------------------
# WeekArchiveView — Animals added in a specific week
# ---------------------------------------------------------------------------
class AnimalWeekArchiveView(WeekArchiveView):
    """
    WeekArchiveView filters by year + week number from the URL
    (e.g. /archive/2024/week/12/).
    week_format='%W' uses Monday-based week numbers (0–53).

    Extra context added:
      - page_title: includes the week number and year
      - animal_count: number of animals added that week
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_archive_week.html"
    week_format = "%W"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = (
            f"Animals Added in Week {self.get_week()}, {self.get_year()}"
        )
        context["animal_count"] = context["object_list"].count()
        return context


# ---------------------------------------------------------------------------
# DayArchiveView — Animals added on a specific day
# ---------------------------------------------------------------------------
class AnimalDayArchiveView(DayArchiveView):
    """
    DayArchiveView filters by year + month + day from the URL
    (e.g. /archive/2024/3/15/).

    Extra context added:
      - page_title: includes the full formatted date
      - animal_count: number of animals added on that day
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_archive_day.html"
    month_format = "%m"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = (
            f"Animals Added on {context['day'].strftime('%B %d, %Y')}"
        )
        context["animal_count"] = context["object_list"].count()
        return context


# ---------------------------------------------------------------------------
# TodayArchiveView — Animals added today
# ---------------------------------------------------------------------------
class AnimalTodayArchiveView(TodayArchiveView):
    """
    TodayArchiveView works exactly like DayArchiveView but automatically
    uses today's date — no date segments are needed in the URL (/archive/today/).
    It reuses the same day template since the context variables are identical.

    Extra context added:
      - page_title: says "Today"
      - animal_count: number of animals added today
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_archive_day.html"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Animals Added Today"
        context["animal_count"] = context["object_list"].count()
        return context


# ---------------------------------------------------------------------------
# DateDetailView — Single animal verified by date + pk
# ---------------------------------------------------------------------------
class AnimalDateDetailView(DateDetailView):
    """
    DateDetailView retrieves a single object using both its pk AND the
    date_field value embedded in the URL. This prevents URL enumeration:
    the date in the URL must match the animal's actual date_added or
    Django returns a 404.

    URL example: /archive/2024/3/15/7/

    It reuses animal_detail.html since it passes the same context variables
    as DetailView ('animal', 'is_elderly', 'weight_category').

    Extra context added:
      - page_title: includes the animal's name
      - is_elderly: derived boolean (same as DetailView)
      - weight_category: derived label (same as DetailView)
    """

    model = Animal
    date_field = "date_added"
    template_name = "animals/animal_detail.html"
    context_object_name = "animal"
    month_format = "%m"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        animal = self.get_object()
        context["page_title"] = f"Animal: {animal.name} (Archive)"
        context["is_elderly"] = animal.age > 15
        context["weight_category"] = AnimalDetailView._weight_category(animal.weight)
        return context
