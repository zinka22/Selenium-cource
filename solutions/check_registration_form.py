# Задание содержится в tasks/check_registration_form.md

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/registration1.html")

    # Ваш код, который заполняет обязательные поля
    input_name = browser.find_element(By.CLASS_NAME, "form-control.first")
    input_name.send_keys("Ivan")
    input_surname = browser.find_element(By.CLASS_NAME, "form-control.second")
    input_surname.send_keys("Petrov")
    input_email = browser.find_element(By.CLASS_NAME, "form-control.third")
    input_email.send_keys("nn@mailto.plus")

    # Отправляем заполненную форму
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    welcome_text_element = WebDriverWait(browser, 15).until(
        ec.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_element.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    helpers.wait_ten_seconds_and_close(browser)
