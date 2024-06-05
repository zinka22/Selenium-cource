# Задание содержится в tasks/switch_to_window.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(
        link="http://suninjuly.github.io/redirect_accept.html"
    )
    magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    magic_button.click()

    browser.switch_to.window(browser.window_handles[1])

    input_value = browser.find_element(By.ID, "input_value")
    element_x_int = int(input_value.text)
    math_result = helpers.solve_math_expression_for_captcha(element_x_int)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(math_result)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
