import pytest
from test.test_base import BaseTest
from pages.loginpage import loginpage
from config.config import TestData
from test.conftest import init_driver
from selenium import webdriver




class Test_login(BaseTest):
    def test_signup_linkvisible(self,init_driver):
        self.init_driver=init_driver
        self.driver=webdriver.chrome
        self.loginpage= loginpage(self,init_driver)
        flag = self.loginpage.is_signup_link_exist()
        assert flag
    def test_login_page_title(self,init_driver):
        self.init_driver=init_driver
        self.loginpage =loginpage(self.init_driver)
        title= self.loginpage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert  title==TestData.LOGIN_PAGE_TITLE
    def test_login(self,init_driver):
        self.init_driver=init_driver
        self.loginpage=loginpage(self.init_driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.PASSWORD)
import pytest
from test.test_base import BaseTest
from pages.loginpage import loginpage
from config.config import TestData
from test.conftest import init_driver



class Test_login(BaseTest):

        def test_login(self,init_driver):
                self.init_driver=init_driver
                self.loginpage=loginpage(self.init_driver)
                self.loginpage.do_login(TestData.USER_NAME,TestData.PASSWORD)






        def test_login_page_title(self,init_driver):
                self.init_driver=init_driver
                self.loginpage =loginpage(self.init_driver)
                title= self.loginpage.get_login_page_title("HubSpot | Redirecting...")
                assert  title=="HubSpot | Redirecting..."


