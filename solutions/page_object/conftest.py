import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome, firefox, edge",
        choices=("chrome", "firefox", "edge"),
    )
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: es or fr",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    match browser_name:
        case "chrome":
            options = ChromeOptions()
            options.add_experimental_option(
                "prefs", {"intl.accept_languages": user_language}
            )
            browser = webdriver.Chrome(options=options)
        case "firefox":
            options = FirefoxOptions()
            options.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(options=options)
        case "edge":
            options = EdgeOptions()
            options.add_experimental_option(
                "prefs", {"intl.accept_languages": user_language}
            )
            browser = webdriver.Edge(options=options)

    browser.implicitly_wait(15)
    yield browser
    browser.quit()
