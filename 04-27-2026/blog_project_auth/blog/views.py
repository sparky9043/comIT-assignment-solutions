from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import View, TemplateView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from .models import Post
from .forms import RegisterForm


# ---------------------------------------------------------------------------
# Auth views
# ---------------------------------------------------------------------------


class CustomLoginView(LoginView):
    template_name = "blog/login.html"


class CustomLogoutView(LogoutView):
    # LogoutView handles GET and POST; LOGOUT_REDIRECT_URL in settings
    # controls where the user lands after logging out.
    pass


class RegisterView(FormView):
    template_name = "blog/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# Blog views — all protected with LoginRequiredMixin
# ---------------------------------------------------------------------------


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-date_created")
        return context


class PostListView(LoginRequiredMixin, TemplateView):
    template_name = "blog/partials/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-date_created")
        return context


class PostCreateView(LoginRequiredMixin, View):
    def post(self, request):
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        if author and title and content:
            Post.objects.create(
                user=request.user,
                author=author,
                title=title,
                content=content,
            )
        posts = Post.objects.all().order_by("-date_created")
        html = render_to_string(
            "blog/partials/post_list.html",
            {"posts": posts},
            request=request,
        )
        return HttpResponse(html)


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            raise Http404
        html = render_to_string(
            "blog/partials/post_edit_form.html",
            {"post": post},
            request=request,
        )
        return HttpResponse(html)


class PostUpdateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            raise Http404
        post.author = request.POST.get("author", post.author)
        post.title = request.POST.get("title", post.title)
        post.content = request.POST.get("content", post.content)
        post.save()
        html = render_to_string(
            "blog/partials/post_item.html",
            {"post": post},
            request=request,
        )
        return HttpResponse(html)


class PostDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            raise Http404
        post.delete()
        return HttpResponse("")


class PostSearchView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get("q", "")
        posts = Post.objects.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(content__icontains=query)
        ).order_by("-date_created")
        html = render_to_string(
            "blog/partials/post_list.html",
            {"posts": posts},
            request=request,
        )
        return HttpResponse(html)
