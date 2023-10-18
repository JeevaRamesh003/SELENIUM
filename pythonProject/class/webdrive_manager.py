from selenium import webdriver
from selenium.webdriver.chrome.service import service
"""from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time"""
Service=service(executable_path="./chromedriver.exe")

option = webdriver.Chrome()
"""C:\python\pycharm works\pythonProject\driver\chromedriver-win64.exe/") (ChromeDriverManager().install())"""
"""driver.implicitly_wait(14000)"""
driver=Chrome(service=service,option=option)
driver.get("https://www.amazon.in/")
"""obj=  driver.find_element(By.ID,"searchDropdownBox")
select= Select(obj)
select.select_by_visible_text("Amazon Fashion")"""
driver.quit()