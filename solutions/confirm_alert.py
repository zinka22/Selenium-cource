# Задание содержится в tasks/confirm_alert.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/alert_accept.html")

    magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    magic_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input_value = browser.find_element(By.ID, "input_value").text
    function_value = helpers.get_math_function_value(input_value)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(function_value)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
