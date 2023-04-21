import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class SearchResultPage(Page):

    SUNSCREEN_PRODUCT = (By.XPATH, "//a[@href='/collections/sun-protection/products/sunscreen-spf-30']/span[text()='SPF30 Sunscreen']")


    def verify_sunscreen_product(self, *locator):
        self.wait_for_element_click(*self.SUNSCREEN_PRODUCT)


