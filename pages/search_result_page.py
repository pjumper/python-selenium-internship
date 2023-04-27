from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultPage(Page):
    SUNSCREEN_PRODUCT = (By.XPATH, "//a[@href='/collections/sun-protection/products/sunscreen-spf-30' and @class='full-unstyled-link']")
    SEARCH_NO_RESULTS = (By.ID, 'ProductCount')
    CLICK_NO_RESULTS_DROPDOWN = (By.CSS_SELECTOR, '.predictive-search__item--term')
    NO_RESULTS_MESSAGE = (By.ID, 'ProductCount')
    CLICK_PRODUCT = (By.CSS_SELECTOR, '#predictive-search-option-1')

    def verify_sunscreen_product(self, expected_result):
        actual_result = self.find_element(*self.SUNSCREEN_PRODUCT).text
        assert expected_result in actual_result, f'Expected {expected_result} and got {actual_result}'


    def verify_no_results(self, expected_result):
        actual_result = self.wait_for_element_appear(*self.SEARCH_NO_RESULTS).text
        print(actual_result)
        assert expected_result in str(actual_result), f'Expected {expected_result} and got {actual_result}'

    def click_no_results_dropdown(self, *locator):
        self.click(*self.CLICK_NO_RESULTS_DROPDOWN)

    def verify_no_results_message_displayed(self, expected_amount, *locator):
        actual_amount = self.driver.find_element(*self.NO_RESULTS_MESSAGE).text
        assert expected_amount in actual_amount, f'Expected {expected_amount} and got {actual_amount}'


    def click_on_product(self, *locator):
        self.click(*self.CLICK_PRODUCT)






