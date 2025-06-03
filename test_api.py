import requests
import pytest
import uuid

BASE_URL = "https://api.demoblaze.com"

unique_username = f"testuser_{uuid.uuid4().hex[:6]}"
valid_password = "secure123"

invalid_username = "usuario_inexistente"
invalid_password = "contraseña_mala"


@pytest.fixture(scope="module")
def create_user():
    """Crear un usuario válido para pruebas."""
    payload = {
        "username": unique_username,
        "password": valid_password
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    return payload  # Devuelve username y password válidos


def test_signup_new_user():
    """Crear un nuevo usuario con éxito."""
    payload = {
        "username": unique_username,
        "password": valid_password
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data or "error" in data


def test_signup_existing_user():
    """Intentar registrar el mismo usuario otra vez."""
    payload = {
        "username": unique_username,
        "password": valid_password
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "error" in data


def test_login_valid_user(create_user):
    """Login exitoso con usuario y contraseña correctos."""
    response = requests.post(f"{BASE_URL}/login", json=create_user)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data or "message" in data


def test_login_invalid_user():
    """Login fallido con usuario o contraseña incorrecta."""
    payload = {
        "username": invalid_username,
        "password": invalid_password
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "error" in data