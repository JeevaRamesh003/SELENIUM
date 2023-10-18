from selenium.webdriver.common.by import By
from pages.Basepage import Basepage
from config.config import TestData
from selenium import webdriver


class loginpage(Basepage):


    EMAIL=(By.ID,"username")
    PASSWORD=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"loginBtn")
    SIGNUP_LINK=(By.LINK_TEXT,"sign up")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self,title):
        return self.driver.title


    def do_login(self,username,password):
        self.do_send_key(self.EMAIL,username)
        self.do_send_key(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)


