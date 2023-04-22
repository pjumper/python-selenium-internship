from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Verify the first product in Sunscreen')
def verify_first_sunscreen_product(context):
    context.app.search_result_page.verify_sunscreen_product()