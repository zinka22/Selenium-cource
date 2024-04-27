import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import solve_captcha

browser = None

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_element_x = browser.find_element(value="input_value")
    element_x_text = int(find_element_x.text)
    math_result = solve_captcha(element_x_text)

    answer_form = browser.find_element(value="answer")
    answer_form.send_keys(math_result)

    robot_checkbox = browser.find_element(value="robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(value="robotsRule")
    robot_radiobutton.click()

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit() if browser else ...
