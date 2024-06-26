# Задание содержится в tasks/execute_script_scroll.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/execute_script.html")

    input_value = browser.find_element(value="input_value").text
    function_value = helpers.get_math_function_value(input_value)

    answer_form = browser.find_element(value="answer")
    answer_form.send_keys(function_value)

    robot_checkbox = browser.find_element(value="robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(value="robotsRule")
    robot_radiobutton.click()

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
