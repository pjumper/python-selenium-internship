import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SearchResultPage(Page):
    SUNSCREEN_PRODUCT = (By.XPATH, "//a[@href='/collections/sun-protection/products/sunscreen-spf-30' and @class='full-unstyled-link']")
    SEARCH_NO_RESULTS = (By.XPATH, "//span[contains(text(), '0 results found') and @class='hidden']")
    CLICK_NO_RESULTS_DROPDOWN = (By.CSS_SELECTOR, '.predictive-search__item--term')
    NO_RESULTS_MESSAGE = (By.ID, 'ProductCount')
    def verify_sunscreen_product(self, *locator):
        self.click(*self.SUNSCREEN_PRODUCT)

    def verify_no_results(self, *locator):
        no_result = self.driver.find_element(*self.SEARCH_NO_RESULTS)
        assert no_result, f'Result is 0'

    def click_no_results_dropdown(self, *locator):
        self.click(*self.CLICK_NO_RESULTS_DROPDOWN)

    def verify_no_results_message_displayed(self, expected_amount, *locator):
        actual_amount = self.driver.find_element(*self.NO_RESULTS_MESSAGE).text
        assert expected_amount in actual_amount, f'Expected {expected_amount} and got {actual_amount}'


