from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


breadcrumb_title_loc = (By.CSS_SELECTOR, "span[class='d-inline-block']")
custom_legs_checkbox_loc = (By.CSS_SELECTOR, "div[class='flex-column mb-3'] label[for='1-7']")
custom_item_loc = (By.CSS_SELECTOR, "a.text-primary.text-decoration-none")
item_loc = (By.XPATH, "(//td[@class='oe_product'])[1]")
add_to_cart_loc = (By.CSS_SELECTOR, "a[aria-label='Shopping cart']")
continue_shopping_btn = (By.CSS_SELECTOR, "div.modal.o_legacy_dialog button.btn.btn-secondary")
cart_quantity_loc = (By.CLASS_NAME, "my_cart_quantity")


class CatalogCatPage(BasePage):
    page_url = 'shop/category/desks-1'

    def check_breadcrumbs(self, text):
        breadcrumb_title = self.find(breadcrumb_title_loc)
        assert breadcrumb_title.text == text

    def check_custom_legs(self, text):
        custom_legs_checkbox = self.find(custom_legs_checkbox_loc)
        custom_legs_checkbox.click()
        customized_item_loc = self.find(custom_item_loc)
        assert customized_item_loc.text == text

    def add_to_cart(self):
        item = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(item_loc))
        # наводим мышь на товар
        ActionChains(self.driver).move_to_element(item).perform()
        # ищем иконку корзины внутри товара
        add_to_cart = item.find_element(*add_to_cart_loc)
        # добавляем в корзину
        ActionChains(self.driver).move_to_element(add_to_cart).click().perform()
        # продолжить покупки
        continue_shopping = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(continue_shopping_btn)
        )
        continue_shopping.click()

    def check_cart_quantity(self, expected_quantity):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(cart_quantity_loc, str(expected_quantity)))
