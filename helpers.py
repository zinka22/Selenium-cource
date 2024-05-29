import time
from math import log, sin
from pathlib import Path

from selenium import webdriver


def solve_math_expression_for_captcha(x: int):
    """Calculate math expression, which value
    will be used to solve captcha
    """
    return str(log(abs(12 * sin(x))))


def open_browser_page(link):
    """Call Chrome browser,
    then open link in browser
    """
    browser = webdriver.Chrome()
    browser.get(link)
    return browser


def run_py_file(filename: str):
    """Execute the given source of python code."""
    exec(Path(filename).read_bytes()) if filename.endswith(".py") else ...


def wait_ten_seconds_and_close(browser):
    """Make wait for ten seconds,
    then quit browser with opened page/pages
    """
    if browser:
        time.sleep(10)
        browser.quit()
