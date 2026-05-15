# store/middleware.py
from django.shortcuts import redirect

EXEMPT = ("/login",)  # paths that don't need a token


class JWTSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not any(request.path.startswith(e) for e in EXEMPT):
            if not request.session.get("token"):
                return redirect("/login/")
        return self.get_response(request)
