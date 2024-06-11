# Задание содержится в tasks/check_registration_with_bugs.md

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import helpers

browser = None
try:
    browser = helpers.open_browser_page(link=f"{helpers.base_url}/registration2.html")

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(
        By.CSS_SELECTOR, '[class="form-control first"]:required'
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR, '[class="form-control second"]:required'
    )
    input2.send_keys("Petrov")
    input3 = browser.find_element(
        By.CSS_SELECTOR, '[class="form-control third"]:required'
    )
    input3.send_keys("nn@mailto.plus")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = WebDriverWait(browser, 15).until(
        ec.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    helpers.wait_ten_seconds_and_close(browser)
