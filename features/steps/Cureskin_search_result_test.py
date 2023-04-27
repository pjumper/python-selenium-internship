from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@when('Verify no results {expected_result} returned on the drop-down')
def verify_no_result_found(context, expected_result):
    # from time import sleep
    # sleep(10)
    context.app.search_result_page.verify_no_results(expected_result)

@when('Click on search button on the drop-down')
def click_no_results_dropdown(context):
    context.app.search_result_page.click_no_results_dropdown()


@when('Click on product')
def click_on_product(context):
    context.app.search_result_page.click_on_product()


@then('Verify the first product in {expected_result}')
def verify_first_sunscreen_product(context, expected_result):
    context.app.search_result_page.verify_sunscreen_product(expected_result)


@then('Verify No results {expected_amount} found message is shown')
def verify_no_results_message_displayed(context, expected_amount):
    context.app.search_result_page.verify_no_results_message_displayed(expected_amount)
