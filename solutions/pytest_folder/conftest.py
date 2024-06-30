import json
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose language: es or fr",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)

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


pytest.register_assert_rewrite("helpers.py")
