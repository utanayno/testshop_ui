from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cart_quantity_loc = (By.CLASS_NAME, "my_cart_quantity")

class BasePage:
    base_url = "http://testshop.qa-practice.com/"
    # текущий урл для страницы
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def check_cart_quantity(self, expected_quantity):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                cart_quantity_loc,
                str(expected_quantity)
            )
        )
