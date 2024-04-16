import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = None


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    magic_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    find_element_x = browser.find_element(By.ID, "input_value")
    element_x_text = int(find_element_x.text)
    math_result = calc(element_x_text)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(math_result)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit() if browser else ...
