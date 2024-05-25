# Задание содержится в tasks/expected_conditions.md


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import helpers

browser = None
try:
    browser = helpers.open_browser_page(
        link="http://suninjuly.github.io/explicit_wait2.html"
    )
    check_for_correct_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    element_x_int = int(browser.find_element(By.ID, "input_value").text)
    math_result = helpers.solve_math_expression_for_captcha(element_x_int)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(math_result)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)

