# Задание содержится в tasks/fill_the_huge_form.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(
        link="http://suninjuly.github.io/huge_form.html"
    )

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Наташа Умница")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
