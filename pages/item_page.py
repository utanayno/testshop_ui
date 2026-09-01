from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

item_title_loc = (By.TAG_NAME, "h1")
terms_link_loc = (By.CSS_SELECTOR, "[href='/terms']")
terms_title_loc = (By.TAG_NAME, "h1")
quantity_field_loc = (By.CSS_SELECTOR, "input.form-control.quantity")
cart_button_loc = (By.ID, "add_to_cart_wrap")
cart_quantity_loc = (By.CLASS_NAME, "my_cart_quantity")

class ItemPage(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def check_item_title(self, text):
        item_title = self.find(item_title_loc)
        assert item_title.text == text

    def open_terms_and_conditions(self):
        terms_link = self.find(terms_link_loc)
        terms_link.click()

    def check_terms_page_title(self):
        terms_title = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        assert terms_title.text == "STANDARD TERMS AND CONDITIONS OF SALE"

    def enter_quantity(self, quantity):
        quantity_field = self.find(quantity_field_loc)
        quantity_field.clear()
        quantity_field.send_keys(quantity)

    def add_to_cart(self):
        cart_button = self.find(cart_button_loc)
        cart_button.click()

    def check_cart_quantity(self, expected_quantity):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                cart_quantity_loc,
                str(expected_quantity)
            )
        )
