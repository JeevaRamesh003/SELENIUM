from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
"""this class is parent of all page"""
class Basepage:
    def __init__(self, driver):
       self.driver= driver

    def do_click(self, by_locator):
       a= WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_located(by_locator))
       a.click()
    def do_send_key(self, by_locator, text):
        a=WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_located(by_locator))
        a.send_keys()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_located(by_locator))
        return element.text


