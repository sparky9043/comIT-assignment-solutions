import requests
from django.conf import settings

API = settings.API_BASE_URL


def _h(token):
    """Build Authorization header."""
    return {"Authorization": f"Bearer {token}"}


# ── Auth ──────────────────────────────────────────────────────────────────────


def get_token(username, password):
    """Return (access_token, is_admin) or raise on failure."""
    resp = requests.post(
        f"{API}/token/", json={"username": username, "password": password}
    )
    resp.raise_for_status()
    token = resp.json()["access"]

    # Detect admin: Send an empty payload to the restricted endpoint.
    # Customers get 403 (Permission Denied).
    # Admins bypass permissions but get 400 (Bad Request - missing fields).
    probe = requests.post(f"{API}/fruits/", json={}, headers=_h(token))

    is_admin = probe.status_code == 400

    return token, is_admin


# ── Fruits ────────────────────────────────────────────────────────────────────


def list_fruits(token):
    return requests.get(f"{API}/fruits/", headers=_h(token)).json()


def get_fruit(token, pk):
    return requests.get(f"{API}/fruits/{pk}/", headers=_h(token)).json()


def create_fruit(token, data):
    return requests.post(f"{API}/fruits/", json=data, headers=_h(token))


def update_fruit(token, pk, data):
    return requests.patch(f"{API}/fruits/{pk}/", json=data, headers=_h(token))


def delete_fruit(token, pk):
    return requests.delete(f"{API}/fruits/{pk}/", headers=_h(token))


# ── Carts ─────────────────────────────────────────────────────────────────────


def list_carts(token):
    return requests.get(f"{API}/carts/", headers=_h(token)).json()


def get_cart(token, pk):
    return requests.get(f"{API}/carts/{pk}/", headers=_h(token)).json()


def create_cart(token):
    return requests.post(f"{API}/carts/", json={}, headers=_h(token))


def delete_cart(token, pk):
    return requests.delete(f"{API}/carts/{pk}/", headers=_h(token))


# ── Cart Items ────────────────────────────────────────────────────────────────


def add_item(token, cart_pk, data):
    return requests.post(f"{API}/carts/{cart_pk}/items/", json=data, headers=_h(token))


def update_item(token, cart_pk, item_pk, data):
    return requests.patch(
        f"{API}/carts/{cart_pk}/items/{item_pk}/", json=data, headers=_h(token)
    )


def delete_item(token, cart_pk, item_pk):
    return requests.delete(f"{API}/carts/{cart_pk}/items/{item_pk}/", headers=_h(token))
