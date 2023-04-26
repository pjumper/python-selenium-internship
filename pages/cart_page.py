from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class CartPage(Page):

    ADD_TO_CART = (By.CSS_SELECTOR, '.product-form__submit.button.button--secondary.button--full-width')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, '.link.product-title')
    REMOVE_PRODUCT_CART = (By.CSS_SELECTOR, 'svg.icon.icon-minus')
    CART_EMPTY = (By.CSS_SELECTOR, 'h3.mini-cart__empty-text')
    def click_add_to_cart(self, *locator):
        self.click(*self.ADD_TO_CART)


    def verify_product_in_cart(self, expected_result):
        from time import sleep
        sleep(10)
        actual_result = self.wait_for_element_appear(*self.PRODUCT_IN_CART).text
        assert expected_result == actual_result, f'Expected {expected_result} and got {actual_result}'

    def remove_product_from_cart(self, *locator):
        self.wait_for_element_appear(*self.REMOVE_PRODUCT_CART)


    def verify_cart_empty(self, *locator):
        cart = self.find_element(*self.CART_EMPTY)
        assert cart, f'cart is empty'