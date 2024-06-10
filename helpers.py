import time
from math import log, sin

from selenium import webdriver

base_url = "https://suninjuly.github.io"


def get_math_function_value(x: int | str) -> str:
    """Calculate math expression, which value
    will be used to solve captcha
    """
    return str(log(abs(12 * sin(int(x)))))


def open_browser_page(link):
    """Call Chrome browser,
    then open link in browser
    """
    browser = webdriver.Chrome()
    browser.get(link)
    return browser


def wait_ten_seconds_and_close(browser):
    """Make wait for ten seconds,
    then quit browser with opened page/pages
    """
    if browser:
        time.sleep(10)
        browser.quit()
