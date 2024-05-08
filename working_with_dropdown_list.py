from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import helpers

browser = None
try:
    browser = helpers.open_browser_page(
        link="https://suninjuly.github.io/selects1.html"
    )

    first_number = browser.find_element(value="num1")
    first = first_number.text
    second_number = browser.find_element(value="num2")
    second = second_number.text
    math_result = str(int(first) + int(second))

    select_element = Select(browser.find_element(value="dropdown"))
    select_element.select_by_value(math_result)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
