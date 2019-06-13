__author__ = 'SJI-Dev-10'
import os
import pytest

cwd = os.getcwd()
#driver = webdriver.Chrome('/drivers/chrome/chromedriver.exe')
@pytest.fixture()
def driver(selenium):
    selenium.implicitly_wait(10)
    return selenium

@pytest.fixture(scope="module")
def base_url_live():
    base_url = "http://www.example.com/"
    return base_url