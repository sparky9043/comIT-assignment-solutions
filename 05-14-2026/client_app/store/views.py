from django.shortcuts import render, redirect
from django.contrib import messages
from . import api

# ── Auth ──────────────────────────────────────────────────────────────────────


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            token, is_admin = api.get_token(username, password)
            request.session["token"] = token
            request.session["username"] = username
            request.session["role"] = "admin" if is_admin else "customer"
            return redirect("/dashboard/")
        except Exception:
            messages.error(request, "Invalid credentials.")
    return render(request, "store/login.html")


def logout_view(request):
    request.session.flush()
    return redirect("/login/")


def dashboard(request):
    """Route to role-specific dashboard."""
    if request.session.get("role") == "admin":
        return redirect("/admin-dash/")
    return redirect("/customer-dash/")


# ── Admin – Fruits ─────────────────────────────────────────────────────────────


def admin_fruits(request):
    fruits = api.list_fruits(request.session["token"])
    return render(request, "store/admin/fruits/list.html", {"fruits": fruits})


def admin_fruit_create(request):
    """HTMX: return the updated table row after creation."""
    if request.method == "POST":
        resp = api.create_fruit(
            request.session["token"],
            {
                "name": request.POST["name"],
                "weight_kg": request.POST["weight_kg"],
                "price_per_kg": request.POST["price_per_kg"],
            },
        )
        if resp.status_code == 201:
            fruit = resp.json()
            return render(request, "store/admin/fruits/_row.html", {"fruit": fruit})
        return render(
            request,
            "store/admin/fruits/_form.html",
            {"error": resp.json(), "action": "create"},
        )
    # GET: return empty form partial
    return render(request, "store/admin/fruits/_form.html", {"action": "create"})


def admin_fruit_edit(request, pk):
    """HTMX: inline edit row → save → return updated row."""
    token = request.session["token"]
    if request.method == "POST":
        resp = api.update_fruit(
            token,
            pk,
            {
                "name": request.POST["name"],
                "weight_kg": request.POST["weight_kg"],
                "price_per_kg": request.POST["price_per_kg"],
            },
        )
        fruit = resp.json()
        return render(request, "store/admin/fruits/_row.html", {"fruit": fruit})
    # GET: return editable form row
    fruit = api.get_fruit(token, pk)
    return render(
        request, "store/admin/fruits/_form.html", {"fruit": fruit, "action": "edit"}
    )


def admin_fruit_delete(request, pk):
    """HTMX: delete and return empty string to remove the row."""
    if request.method == "DELETE":
        api.delete_fruit(request.session["token"], pk)
        return render(request, "store/admin/fruits/_row.html", {"deleted": True})


# ── Admin – Carts ──────────────────────────────────────────────────────────────


def admin_carts(request):
    token = request.session["token"]
    carts = api.list_carts(token)
    fruits = api.list_fruits(token)
    return render(
        request, "store/admin/carts/list.html", {"carts": carts, "fruits": fruits}
    )


def admin_cart_create(request):
    if request.method == "POST":
        token = request.session["token"]  # Extract token
        resp = api.create_cart(token)
        cart = resp.json()
        fruits = api.list_fruits(token)  # Fetch fruits list

        # Pass 'fruits' in the context dictionary
        return render(
            request,
            "store/admin/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},
        )


def admin_cart_delete(request, pk):
    if request.method == "DELETE":
        api.delete_cart(request.session["token"], pk)
        return render(request, "store/admin/carts/_cart_card.html", {"deleted": True})


# store/views.py


def admin_item_add(request, cart_pk):
    if request.method == "POST":
        token = request.session["token"]
        api.add_item(
            token,
            cart_pk,
            {
                "fruit": request.POST["fruit"],
                "quantity_kg": request.POST["quantity_kg"],
            },
        )
        cart = api.get_cart(token, cart_pk)
        fruits = api.list_fruits(token)  # <-- ADD THIS

        return render(
            request,
            "store/admin/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},  # <-- ADD THIS
        )


def admin_item_update(request, cart_pk, item_pk):
    if request.method == "POST":
        token = request.session["token"]
        api.update_item(
            token, cart_pk, item_pk, {"quantity_kg": request.POST["quantity_kg"]}
        )
        cart = api.get_cart(token, cart_pk)
        fruits = api.list_fruits(token)  # <-- ADD THIS

        return render(
            request,
            "store/admin/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},  # <-- ADD THIS
        )


def admin_item_delete(request, cart_pk, item_pk):
    if request.method == "DELETE":
        token = request.session["token"]
        api.delete_item(token, cart_pk, item_pk)
        cart = api.get_cart(token, cart_pk)
        fruits = api.list_fruits(token)  # <-- ADD THIS

        return render(
            request,
            "store/admin/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},  # <-- ADD THIS
        )


# ── Customer – Fruits (read-only) ─────────────────────────────────────────────


def customer_dashboard(request):
    token = request.session["token"]
    fruits = api.list_fruits(token)
    carts = api.list_carts(token)
    return render(
        request, "store/customer/dashboard.html", {"fruits": fruits, "carts": carts}
    )


# ── Customer – Carts ──────────────────────────────────────────────────────────


def customer_cart_create(request):
    if request.method == "POST":
        token = request.session["token"]
        resp = api.create_cart(token)
        cart = resp.json()
        fruits = api.list_fruits(token)
        return render(
            request,
            "store/customer/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},
        )


def customer_cart_delete(request, pk):
    if request.method == "DELETE":
        api.delete_cart(request.session["token"], pk)
        return render(
            request, "store/customer/carts/_cart_card.html", {"deleted": True}
        )


def customer_item_add(request, cart_pk):
    if request.method == "POST":
        token = request.session["token"]
        api.add_item(
            token,
            cart_pk,
            {
                "fruit": request.POST["fruit"],
                "quantity_kg": request.POST["quantity_kg"],
            },
        )
        cart = api.get_cart(token, cart_pk)
        fruits = api.list_fruits(token)
        return render(
            request,
            "store/customer/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},
        )


def customer_item_update(request, cart_pk, item_pk):
    if request.method == "POST":
        token = request.session["token"]
        api.update_item(
            token, cart_pk, item_pk, {"quantity_kg": request.POST["quantity_kg"]}
        )
        cart = api.get_cart(token, cart_pk)
        fruits = api.list_fruits(token)
        return render(
            request,
            "store/customer/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},
        )


def customer_item_delete(request, cart_pk, item_pk):
    if request.method == "DELETE":
        token = request.session["token"]
        api.delete_item(token, cart_pk, item_pk)
        cart = api.get_cart(token, cart_pk)
        fruits = api.list_fruits(token)
        return render(
            request,
            "store/customer/carts/_cart_card.html",
            {"cart": cart, "fruits": fruits},
        )
