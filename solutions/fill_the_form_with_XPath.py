# Задание содержится в tasks/fill_the_form_with_XPath.md

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/find_xpath_form")

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Наташа Умница")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
