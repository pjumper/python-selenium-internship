from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('Adjust the price filter so change in number of product')
def hover_price_filter(context):
    context.app.product_page.hover_price_filter()






