from selenium import webdriver
import pytest
from application import Application

@pytest.fixture
def app(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver)