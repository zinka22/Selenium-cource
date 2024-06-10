from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/math.html")

    input_value = int(
        browser.find_element(By.CSS_SELECTOR, ".form-group #input_value").text
    )
    function_value = helpers.get_math_function_value(input_value)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    input1.send_keys(function_value)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
