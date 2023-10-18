import py
import pytest
from selenium import webdriver
from config.config import TestData

from selenium.webdriver.chrome.options import Options


import config.config





@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--start-maximized")

        # Specify the path to the ChromeDriver executable
        chrome_executable_path = TestData.CHROME_EXECUTABLE_PATH

        options.add_argument(f"--chromedriver-executable={chrome_executable_path}")

        web_driver = webdriver.Chrome(options=options)
        yield web_driver
        web_driver.quit()

