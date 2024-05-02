import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import solve_math_expression_for_captcha

browser = None

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    magic_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    find_element_x = browser.find_element(By.ID, "input_value")
    element_x_int = int(find_element_x.text)
    math_result = solve_math_expression_for_captcha(element_x_int)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(math_result)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit() if browser else ...
