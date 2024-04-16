import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = None


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field_name = browser.find_element(By.NAME, "firstname")
    field_name.send_keys("Ivan")

    field_last_name = browser.find_element(By.NAME, "lastname")
    field_last_name.send_keys("Ivanov")

    field_email = browser.find_element(By.NAME, "email")
    field_email.send_keys("Ivanov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test__file_for_uploading.txt")

    choose_file_button = browser.find_element(By.NAME, "file")
    choose_file_button.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit() if browser else ...
