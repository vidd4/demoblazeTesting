import pytest
import requests
import uuid
from pytest_bdd import scenarios, given, when, then
import allure


BASE_URL = "https://api.demoblaze.com"
scenarios('../features/login_api.feature')


unique_username = f"testuser_{uuid.uuid4().hex[:6]}"
valid_password = "secure123"
invalid_username = "usuario_inexistente"
invalid_password = "contraseña_mala"

response_data = {}

@allure.suite("Login API Suite")
@allure.title("Test Login API")
def test_login_api():
    pass

@pytest.fixture(scope="module")
def existing_user():
    payload = {"username": unique_username, "password": valid_password}
    requests.post(f"{BASE_URL}/signup", json=payload)
    return payload


@allure.step("Tengo un nombre de usuario único y contraseña válidos")
@given("I have a unique valid username and password")
def create_unique_user():
    response_data["payload"] = {"username": unique_username, "password": valid_password}


@allure.step("Ya he registrado al mismo usuario")
@given("I have already registered the same user")
def reuse_existing_user(existing_user):
    response_data["payload"] = existing_user


@allure.step("Soy un usuario registrado")
@given("I am a registered user")
def registered_user(existing_user):
    response_data["payload"] = existing_user


@allure.step("No soy un usuario registrado")
@given("I am not a registered user")
def unregistered_user():
    response_data["payload"] = {"username": invalid_username, "password": invalid_password}


@allure.step("Envio una solicitud de registro")
@when("I send a signup request")
def signup():
    res = requests.post(f"{BASE_URL}/signup", json=response_data["payload"])
    response_data["response"] = res


@allure.step("Intento registrarme nuevamente")
@when("I try to sign up again")
def signup_again():
    res = requests.post(f"{BASE_URL}/signup", json=response_data["payload"])
    response_data["response"] = res


@allure.step("Envio una solicitud de inicio de sesión con credenciales válidas")
@when("I send a login request with correct credentials")
def login_valid():
    res = requests.post(f"{BASE_URL}/login", json=response_data["payload"])
    response_data["response"] = res


@allure.step("Envio una solicitud de inicio de sesión con credenciales incorrectas")
@when("I send a login request with incorrect credentials")
def login_invalid():
    res = requests.post(f"{BASE_URL}/login", json=response_data["payload"])
    response_data["response"] = res


@allure.step("Debería recibir un mensaje de éxito o que el usuario ya existe")
@then("I should receive a success message or user already exists")
def check_signup_success():
    res = response_data["response"]
    assert res.status_code == 200
    data = res.json()
    assert "message" in data or "error" in data


@allure.step("Debería recibir un mensaje de error")
@then("I should receive an error message")
def check_error():
    res = response_data["response"]
    assert res.status_code == 200
    data = res.json()
    assert "error" in data


@allure.step("Debería recibir un token o mensaje de éxito")
@then("I should receive a token or success message")
def check_login_success():
    res = response_data["response"]
    assert res.status_code == 200
    data = res.json()
    assert "token" in data or "message" in data
