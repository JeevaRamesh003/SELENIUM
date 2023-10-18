from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service

driver= webdriver.Chrome("C:\chromedriver.exe.exe")

driver.get("https://www.youtube.com/")
print(driver.title)
"""""  def test_signup_linkvisible(self, driver):
      self.init_driver = driver
      time.sleep(10)
      driver.implicitly_wait(10)
      flag = self.is_signup_link_exist()
      assert flag"""""
