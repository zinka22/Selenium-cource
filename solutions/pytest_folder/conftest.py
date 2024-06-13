import pytest
from selenium import webdriver
import json


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def auth_data():
    with open("auth_keys_stepik.json", "r") as data:
        auth_data = json.load(data)
        return auth_data
