from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    link = "https://suninjuly.github.io/math.html"
    browser = helpers.open_browser_page(link)

    x_element = browser.find_element(By.CSS_SELECTOR, ".form-group #input_value")
    x = int(x_element.text)
    y = helpers.solve_math_expression_for_captcha(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    input1.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
