from selenium.webdriver.common.by import By

class OrderForm:
    nameInput = (By.XPATH, "//input[@id='name']")
    countryInput = (By.XPATH, "//input[@id='country']")
    cityInput = (By.XPATH, "//input[@id='city']")
    cardInput = (By.XPATH, "//input[@id='card']")
    monthInput = (By.XPATH, "//input[@id='month']")
    yearInput = (By.XPATH, "//input[@id='year']")
    purchaseButton = (By.XPATH, "//button[text()='Purchase']")
    successAlert = (By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']")