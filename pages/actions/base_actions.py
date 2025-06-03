from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BaseActions:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def _wait_for_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return self.driver.find_element(*locator)
        except TimeoutException:
            print("El elemento no fue encontrado")
            return None

    def element_click(self, locator):
        element = self._wait_for_element(locator)
        if element:
            element.click()
        else:
            raise Exception("No se puede hacer click en el elemento")

    def type_info(self, locator, keyword):
        element = self._wait_for_element(locator)
        if element:
            element.send_keys(keyword)
        else:
            raise Exception("No se puede encontrar el elemento")

    def is_displayed(self, locator):
        element = self._wait_for_element(locator)
        if element:
            return element.is_displayed()
        else:
            return False

    def is_enabled(self, locator):
        element = self._wait_for_element(locator)
        if element:
            return element.is_enabled()
        else:
            return False