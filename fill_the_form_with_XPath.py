from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = helpers.open_browser_page(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Наташа Умница")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
