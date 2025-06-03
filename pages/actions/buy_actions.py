from .base_actions import BaseActions
from pages.page_objects.home import Home
from pages.page_objects.cart import Cart
from pages.page_objects.products import Products
from pages.page_objects.order_form import OrderForm
from pages.page_objects.success_alert import SuccessAlert


class BuyActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    def click_product(self):
        self.element_click(Home.productCard1)

    def click_add_cart(self):
        self.element_click(Products.addCartButton)

    def click_cart(self):
        self.element_click(Home.cartButton)

    def click_order(self):
        self.element_click(Cart.orderButton)

    def fill_name(self, name: str):
        self.type_info(OrderForm.nameInput, name)

    def fill_country(self, country: str):
        self.type_info(OrderForm.countryInput, country)

    def fill_city(self, city: str):
        self.type_info(OrderForm.cityInput, city)

    def fill_card(self, card: str):
        self.type_info(OrderForm.cardInput, card)

    def fill_month(self, month: str):
        self.type_info(OrderForm.monthInput, month)

    def fill_year(self, year: str):
        self.type_info(OrderForm.yearInput, year)

    def click_purchase(self):
        self.element_click(OrderForm.purchaseButton)

    def displayed_alert(self):
        return self.is_displayed(OrderForm.successAlert)