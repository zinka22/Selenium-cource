from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    link = "http://suninjuly.github.io/huge_form.html"
    browser = helpers.open_browser_page(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Наташа Умница")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
