from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

cart_page_title_loc = (By.TAG_NAME, 'h3')
empty_cart_alert_loc = (By.CSS_SELECTOR, 'div.js_cart_lines.alert.alert-info')
remove_from_cart_btn_loc = (By.CSS_SELECTOR, '[aria-label="Remove from cart"]')
plus_item_loc = (By.CSS_SELECTOR, 'i.fa.fa-plus.position-relative.z-index-1')
price_item_loc = (By.CSS_SELECTOR, "span[data-oe-type='monetary'] span[class='oe_currency_value']")

class CartPage(BasePage):
    page_url = 'shop/cart'

    def check_cart_title_is(self, text):
        cart_title = self.find(cart_page_title_loc)
        assert cart_title.text == text

    def check_cart_alert(self, expected_cart_alert):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                empty_cart_alert_loc,
                expected_cart_alert
            )
        )

    def delete_item_from_cart(self):
        remove_from_cart_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(remove_from_cart_btn_loc))
        remove_from_cart_btn.click()

    def change_quantity(self):
        plus_item = self.find(plus_item_loc)
        plus_item.click()

    def check_item_price(self, expected_price):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                price_item_loc,
                expected_price
            )
        )
