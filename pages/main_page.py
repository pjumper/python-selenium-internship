from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):


    CLOSE_POPUP = (By.CSS_SELECTOR, '.popup-close')
    def open_main(self):
        self.open_url('https://shop.cureskin.com/')

    def close_popup(self):
        self.wait_for_element_click(*self.CLOSE_POPUP)
        sleep(5)