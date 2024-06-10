# Задание содержится в tasks/fill_the_huge_form.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/huge_form.html")

    text_fields = browser.find_elements(By.TAG_NAME, "input")
    for field in text_fields:
        field.send_keys("Наташа Умница")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
