from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ALL_PRICES = (By.CSS_SELECTOR, ".price-item.price-item--sale price-money")
FILTER_PRICE = (By.CSS_SELECTOR,  ".facets__price > div")

@when('Adjust the price filter so change in number of product')
def hover_price_filter(context):
    context.driver.original_number_of_products = len(context.driver.find_elements(*ALL_PRICES))
    context.app.product_page.hover_price_filter()
    sleep(10)


@then('Verify number of product changes')
def verify_number_of_products(context):
    actual_number_of_products = len(context.driver.find_elements(*ALL_PRICES))
    assert context.driver.original_number_of_products != actual_number_of_products, f'Expected {context.driver.original_number_of_products} is not diferent to {actual_number_of_products}'

@then('Verify product displayed are within the price filter')
def verify_products_price(context):
    max_price = context.driver.find_element(*FILTER_PRICE).text.replace('Price: Rs. 0 — Rs. ', '')
    all_prices = context.driver.find_elements(*ALL_PRICES)

    for price in all_prices:
        assert float(price.text.replace('Rs.', '')) <= float(max_price), f"Expected {price.text.replace('Rs.', '')} is not lesser than the max price {max_price}"





