import requests
import pytest

BASE_URL = "https://api.demoblaze.com"

signup_data = {
    "username": "usuario_prueba123",
    "password": "clave123"
}

login_data = {
    "username": "usuario_prueba123",
    "password": "clave123"
}


def test_signup():
    url = f"{BASE_URL}/signup"
    response = requests.post(url, json=signup_data)
    assert response.status_code == 200

def test_login():
    url = f"{BASE_URL}/login"
    response = requests.post(url, json=login_data)
    assert response.status_code == 200
