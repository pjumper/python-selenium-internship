from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('Click add to cart')
def click_add_to_cart(context):
    context.app.cart_page.click_add_to_cart()


@when('Verify product in cart')
def verify_product_in_cart(context):
    context.app.cart_page.verify_product_in_cart()


@when('Delete product from cart')
def remove_product_from_cart(context):
    context.app.cart_page.remove_product_from_cart()


@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()