from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Cureskin page')
def open_cureskin_page(context):
    context.app.main_page.open_main()
