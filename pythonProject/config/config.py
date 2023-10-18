from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options



class TestData:


        """service = service(executable_path="C:\python\pycharm works\chromedriver-win64\chromedriver.exe")
        Option = webdriver.Chrome()
        CHROME_EXECUTABLE_PATH =Chrome(service=service,Options=Options)"""
        CHROME_EXECUTABLE_PATH="C:\python\pycharm works\pythonProject\driver\chromedriver.exe"
        driver = webdriver.Chrome()






        BASE_URL="https://app.hubspot.com/"
        USER_NAME="jeevaramesh003@gmail.com"
        PASSWORD="Jeeva@123"
        LOGIN_PAGE_TITLE="HubSpot LOGIN"

