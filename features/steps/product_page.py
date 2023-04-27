from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




@when('Adjust the price filter so change in number of product')
def hover_price_filter(context):
    context.app.product_page.hover_price_filter()
    sleep(5)


@then('Verify number of product changes')
def verify_number_of_products(context):
    context.app.product_page.verify_number_of_products()


@then('Verify product displayed are within the price filter')
def verify_products_price(context):
    context.app.product_page.verify_products_price()





