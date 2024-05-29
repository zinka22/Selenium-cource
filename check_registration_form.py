from time import sleep

from selenium.webdriver.common.by import By

import helpers


def check_registration_form():
    browser = None
    try:
        browser = helpers.open_browser_page(
            link="http://suninjuly.github.io/registration1.html"
        )

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input3.send_keys("nn@mailto.plus")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        helpers.wait_ten_seconds_and_close(browser)


if __name__ == "__main__":
    check_registration_form()
