import json
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def auth_data() -> dict[str, str]:
    """Read login, password from auth_keys_stepic.json file
    and return them as a dictionary.
    """
    auth_path = Path().rglob("auth_keys_stepik.json")
    return json.loads(next(auth_path).read_text())


@pytest.fixture(scope="function")
def user_authorization_checker_factory(browser):
    """Check if user is authorized"""

    def check_if_user_is_authorised():
        try:
            popup_is_closed = WebDriverWait(browser, 5).until(
                ec.invisibility_of_element_located((By.ID, "login_form"))
            )
            return popup_is_closed
        except TimeoutException:
            return False

    return check_if_user_is_authorised
