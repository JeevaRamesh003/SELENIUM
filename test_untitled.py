""""Generated by Selenium IDE"""""
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_untitled(self):
    self.driver.get("https://www.flipkart.com/")
    self.driver.set_window_size(1536, 816)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.NAME, "q").send_keys("IPHONE 15")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) .\\_2kHMtA").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) .\\_2kHMtA").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) .\\_2kHMtA")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) .\\_4rR01T").click()
    self.vars["win749"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win749"])
    self.driver.execute_script("window.scrollTo(0,1626.4000244140625)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AJtlD").click()
    self.driver.find_element(By.LINK_TEXT, "Cart").click()
    element = self.driver.find_element(By.LINK_TEXT, "Login")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.close()
  
