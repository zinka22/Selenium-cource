import json
from pathlib import Path

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def auth_data() -> dict[str, str]:
    """Read login, password from auth_keys_stepic.json file
    and return them as a dictionary.
    """
    auth_path = Path().rglob("auth_keys_stepik.json")
    return json.loads(next(auth_path).read_text())
