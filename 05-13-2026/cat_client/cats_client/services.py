import requests

API_BASE = "http://127.0.0.1:8000/api/cats/"
AUTH = ("admin", "password")  # Replace or load from settings/environment


def get_all_cats():
    response = requests.get(API_BASE, auth=AUTH)
    response.raise_for_status()
    return response.json()


def get_cat(cat_id):
    response = requests.get(f"{API_BASE}{cat_id}/", auth=AUTH)
    response.raise_for_status()
    return response.json()


def create_cat(data):
    response = requests.post(API_BASE, json=data, auth=AUTH)
    response.raise_for_status()
    return response.json()


def update_cat(cat_id, data):
    response = requests.put(f"{API_BASE}{cat_id}/", json=data, auth=AUTH)
    response.raise_for_status()
    return response.json()


def delete_cat(cat_id):
    response = requests.delete(f"{API_BASE}{cat_id}/", auth=AUTH)
    response.raise_for_status()
