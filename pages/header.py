from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):

    SHOP_BY_PRODUCT = (By.XPATH, "//summary[@class='header__menu-item header__menu-item--top list-menu__item focus-inset']/span[text()='Shop by Product']")
    CLICK_SUNSCREEN_TAB = (By.XPATH, "//a[@href='/collections/sun-protection']/span[text()='Sunscreens']")

    def click_shop_by_product(self, *locator):
        self.click(*self.SHOP_BY_PRODUCT)

    def click_sunscreen_tab(self, *locator):
        self.wait_for_element_click(*self.CLICK_SUNSCREEN_TAB)


