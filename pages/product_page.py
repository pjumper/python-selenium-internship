from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductPage(Page):

    PRICE_FILTER = (By.CSS_SELECTOR, '.price-range__thumbs.is-upper')


    def hover_price_filter(self):
        price_filter = self.find_element(*self.PRICE_FILTER)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(price_filter, -100, 0)
        actions.perform()