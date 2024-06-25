# Задание содержится в tasks/upload_file_from_pc.md

from pathlib import Path

from selenium.webdriver.common.by import By

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/file_input.html")

    field_name = browser.find_element(By.NAME, "firstname")
    field_name.send_keys("Ivan")

    field_last_name = browser.find_element(By.NAME, "lastname")
    field_last_name.send_keys("Ivanov")

    field_email = browser.find_element(By.NAME, "email")
    field_email.send_keys("Ivanov@mail.ru")

    file_path = Path("test__file_for_uploading.txt").absolute()

    choose_file_button = browser.find_element(By.NAME, "file")
    choose_file_button.send_keys(str(file_path))

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    helpers.wait_ten_seconds_and_close(browser)
