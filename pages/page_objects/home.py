from selenium.webdriver.common.by import By

class Home:
    homeButton = (By.XPATH, "//a[text()='Home ']")
    cartButton = (By.XPATH, "//a[text()='Cart']")
    productCard1 = (By.XPATH, "(//a[@href='prod.html?idp_=1'])[2]")
    productCard2 = (By.XPATH, "(//a[@href='prod.html?idp_=2'])[2]")
