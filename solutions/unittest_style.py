# Задание содержится в tasks/unittest_style.md

import unittest
from time import sleep

from selenium.webdriver.common.by import By

import helpers


class TestAbs(unittest.TestCase):
    def test_check_registration_form(self):

        browser = None
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
        welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_element
        welcome_text = welcome_text_element.text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Welcome text should be 'Congratulations! You have successfully registered!'",
        )

    def test_check_registration_with_bugs(self):
        browser = None
        browser = helpers.open_browser_page(
            link="http://suninjuly.github.io/registration2.html"
        )

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

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        sleep(1)

        # находим элемент, содержащий текст
        welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_element
        welcome_text = welcome_text_element.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Welcome text should be 'Congratulations! You have successfully registered!'",
        )


if __name__ == "__main__":
    unittest.main()
