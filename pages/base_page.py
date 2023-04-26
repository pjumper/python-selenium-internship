from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_the_element_to_be_visible(self, *locator):
        return self.wait.until(EC.element_to_be_clickable())
    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))

    def wait_for_visibility_of_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located())

    def wait_for_text_to_be_present(self, *locator):
        return self.wait.until(EC.text_to_be_present_in_element())