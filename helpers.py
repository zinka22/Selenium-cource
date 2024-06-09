import time
from math import log, sin

from selenium import webdriver


def get_math_function_value(x: int):
    """Calculate math expression, which value
    will be used to solve captcha
    """
    return str(log(abs(12 * sin(x))))


def open_browser_page(input_param):
    """Call Chrome browser,
    produce the link to target web-site,
    then open link in browser
    """
    browser = webdriver.Chrome()
    link = "".join(["https://suninjuly.github.io/", input_param, ".html"])
    browser.get(link)
    return browser


def wait_ten_seconds_and_close(browser):
    """Make wait for ten seconds,
    then quit browser with opened page/pages
    """
    if browser:
        time.sleep(10)
        browser.quit()
