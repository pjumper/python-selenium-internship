from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class SignInPage(Page):

    def verify_page_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin?')