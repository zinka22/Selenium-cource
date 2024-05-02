import helpers
from selenium.webdriver.common.by import By

browser = None
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = helpers.open_browser_page(link)

    chest_element = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
    x = float(chest_element.get_attribute("valuex"))

    result_function = helpers.solve_math_expression_for_captcha(x)

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(result_function)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    submit_button.click()


finally:
    helpers.wait_ten_seconds_and_close(browser) if browser else ...
