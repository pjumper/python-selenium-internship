from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click on "Shop by product"')
def click_shop_by_product(context):
    context.app.header.click_shop_by_product()


@when('Select sunscreens')
def click_sunscreen_tab(context):
    context.app.header.click_sunscreen_tab()


@when('Click on search button')
def click_search_button(context):
    context.app.header.click_search_button()

@when('Enter a product name {text} that does not exist to search box')
def input_not_product_search(context, text):
    context.app.header.input_text_not_product(text)
    context.driver.find_element(By.CSS_SELECTOR, '.predictive-search__item--term.button.button--small.button--full-width').click()



@when('Enter a product name {text}')
def input_product_name(context, text):
    context.app.header.input_product_name(text)


@when('Click on Shop All section')
def click_shop_all(context):
    context.app.header.click_shop_all()

