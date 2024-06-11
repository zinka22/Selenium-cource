# Задание содержится в tasks/get_attribute.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/get_attribute.html")

    chest_element = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
    input_value = chest_element.get_attribute("valuex")

    function_value = helpers.get_math_function_value(input_value)

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(function_value)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    submit_button.click()


finally:
    helpers.wait_ten_seconds_and_close(browser)
