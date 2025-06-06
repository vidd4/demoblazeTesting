import pytest
import requests
import uuid
from pytest_bdd import scenario, given, when, then
import allure


BASE_URL = "https://api.demoblaze.com"


unique_username = f"testuser_{uuid.uuid4().hex[:6]}"
valid_password = "secure123"
invalid_username = "usuario_inexistente"
invalid_password = "contraseña_mala"

response_data = {}

@allure.suite("Login API Suite")
@allure.title("Sign up a new user successfully")
@scenario('login_api.feature', 'Sign up a new user successfully')
def test_signup_new_user():
    pass

@allure.suite("Login API Suite")
@allure.title("Sign up with an existing user")
@scenario('login_api.feature', 'Sign up with an existing user')
def test_signup_existing_user():
    pass

@allure.suite("Login API Suite")
@allure.title("Log in with valid credentials")
@scenario('login_api.feature', 'Log in with valid credentials')
def test_login_valid():
    pass

@allure.suite("Login API Suite")
@allure.title("Log in with invalid credentials")
@scenario('login_api.feature', 'Log in with invalid credentials')
def test_login_invalid():
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
