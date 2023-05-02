from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductPage(Page):

    PRICE_FILTER = (By.CSS_SELECTOR, '.price-range__thumbs.is-upper')
    ALL_PRICES = (By.CSS_SELECTOR, ".price-item.price-item--sale price-money")
    FILTER_PRICE = (By.CSS_SELECTOR, ".facets__price > div")

    def hover_price_filter(self):
        price_filter = self.find_element(*self.PRICE_FILTER)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(price_filter, -175, 0)
        actions.perform()
        self.driver.original_number_of_products = len(self.driver.find_elements(*self.ALL_PRICES))

    def verify_products_price(self, *locator):
        max_price =self.find_element(*self.FILTER_PRICE).text.replace('Price: Rs. 0 — Rs. ', '')
        all_prices = self.driver.find_elements(*self.ALL_PRICES)

        for price in all_prices:
            assert float(price.text.replace('Rs.', '')) <= float(max_price), f"Expected {price.text.replace('Rs.', '')} is lesser than the max price {max_price}"

    def verify_number_of_products(self, *locator):
        actual_number_of_products = len(self.driver.find_elements(*self.ALL_PRICES))
        assert self.driver.original_number_of_products != actual_number_of_products, f'Expected {self.driver.original_number_of_products} is not diferent to {actual_number_of_products}'