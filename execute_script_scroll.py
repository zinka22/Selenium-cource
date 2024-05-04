from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(
        link="https://SunInJuly.github.io/execute_script.html"
    )
    find_element_x = browser.find_element(value="input_value")
    element_x_int = int(find_element_x.text)
    math_result = helpers.solve_math_expression_for_captcha(element_x_int)

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
    helpers.wait_ten_seconds_and_close(browser)
