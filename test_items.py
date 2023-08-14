import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import item_contains_add_to_cart_button


def test_add_to_cart_button(browser):
    item_contains_add_to_cart_button(browser)
    time.sleep(30)
    add_to_cart_button = WebDriverWait(browser, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
    assert add_to_cart_button , "корзинка не найдена"

