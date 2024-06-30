import time
from math import log, sin

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://suninjuly.github.io"


def assert_if_user_is_authorized_on_lesson_page(browser):
    """Assert function to verify user authorization. Raise an assertion error if the user is not authorized."""
    is_authorized_user = False
    if browser:
        try:
            WebDriverWait(browser, 5).until(
                ec.invisibility_of_element_located((By.ID, "login_form"))
            )
            WebDriverWait(browser, 5).until(
                ec.presence_of_element_located((By.CLASS_NAME, "navbar__profile-img"))
            )
            WebDriverWait(browser, 5).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//*[@data-type='string-quiz']")
                )
            )
            is_authorized_user = True
        except TimeoutException:
            ...
    assert is_authorized_user, "User is guest, the answer can't be sent"


def get_math_function_value(x: int | str) -> str:
    """Calculate math expression, which value will be used to solve captcha."""
    return str(log(abs(12 * sin(int(x)))))


def open_browser_page(link):
    """Create Chrome browser instance, then open link in browser."""
    browser = webdriver.Chrome()
    browser.get(link)
    return browser


def wait_ten_seconds_and_close(browser):
    """Explicit wait for 10 seconds, then quit browser with opened page/pages."""
    if browser:
        time.sleep(10)
        browser.quit()
