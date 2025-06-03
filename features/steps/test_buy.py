import allure
import pytest
from pages.actions.buy_actions import BuyActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pytest_bdd import given, when, then, scenario


@allure.suite("Buy Suite")
@allure.title("Buy a product successfully")
@scenario('buy.feature', 'Buy a product successfully')
def test_buy_product():
    pass


@pytest.fixture
def buy(driver):
    return BuyActions(driver)


@allure.step("Abrir la página principal")
@given("I am on the demoblaze homepage")
def open_homepage(buy):
    buy.load("https://www.demoblaze.com/")


@allure.step("Seleccionar un producto")
@when("I select a product")
def select_product(buy):
    buy.click_product()


@allure.step("Agregar el producto al carrito")
@when("I add the product to the cart")
def add_to_cart(buy):
    buy.click_add_cart()


@allure.step("Aceptar la alerta de confirmación")
@when("I accept the alert")
def accept_alert(driver):
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()


@allure.step("Ir al carrito")
@when("I go to the cart")
def go_to_cart(buy):
    buy.click_cart()


@allure.step("Llenar formulario de compra y realizar el pedido")
@when("I place the order with valid information")
def fill_order_info(buy):
    buy.click_order()
    buy.fill_name("Juan")
    buy.fill_country("Ecuador")
    buy.fill_city("Quito")
    buy.fill_card("1234567890")
    buy.fill_month("Junio")
    buy.fill_year("2025")
    buy.click_purchase()


@allure.step("Verificar mensaje de confirmación")
@then("I should see the confirmation message")
def verify_confirmation(buy, driver):
    try:
        assert buy.displayed_alert()
        allure.attach(driver.get_screenshot_as_png(), name="Compra exitosa", attachment_type=allure.attachment_type.PNG)
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name="Fallo en compra", attachment_type=allure.attachment_type.PNG)
        raise
