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




