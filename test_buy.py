from selenium import webdriver
from pages.actions.buy_actions import BuyActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_buy_product(driver):
    buy = BuyActions(driver)
    buy.load("https://www.demoblaze.com/")
    buy.click_product()
    buy.click_add_cart()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    buy.click_cart()
    buy.click_order()
    buy.fill_name("Juan")
    buy.fill_country("Ecuador")
    buy.fill_city("Quito")
    buy.fill_card("1234567890")
    buy.fill_month("Junio")
    buy.fill_year("2025")
    buy.click_purchase()
    assert buy.displayed_alert()