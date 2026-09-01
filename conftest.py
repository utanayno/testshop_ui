from selenium import webdriver
import pytest
from time import sleep
from pages.cart_page import CartPage
from pages.catalog_category_page import CatalogCatPage
from pages.item_page import ItemPage

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    sleep(3)
    return chrome_driver

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def catalog_category_page(driver):
    return CatalogCatPage(driver)

@pytest.fixture
def item_page(driver):
    return ItemPage(driver)

