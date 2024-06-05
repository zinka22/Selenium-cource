# Задание содержится в tasks/unittest_style.md

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import helpers


class TestAbs(unittest.TestCase):
    def test_check_registration_form(self):
        browser = None
        browser = helpers.open_browser_page(
            link="http://suninjuly.github.io/registration1.html"
        )

        # Ваш код, который заполняет обязательные поля
        input_name = browser.find_element(By.CLASS_NAME, "form-control.first")
        input_name.send_keys("Ivan")
        input_surname = browser.find_element(By.CLASS_NAME, "form-control.second")
        input_surname.send_keys("Petrov")
        input_email = browser.find_element(By.CLASS_NAME, "form-control.third")
        input_email.send_keys("nn@mailto.plus")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_element = WebDriverWait(browser, 15).until(
            ec.presence_of_element_located((By.TAG_NAME, "h1"))
        )

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
        input_name = browser.find_element(
            By.CSS_SELECTOR, '[class="form-control first"]:required'
        )
        input_name.send_keys("Ivan")
        input_surname = browser.find_element(
            By.CSS_SELECTOR, '[class="form-control second"]:required'
        )
        input_surname.send_keys("Petrov")
        input_email = browser.find_element(
            By.CSS_SELECTOR, '[class="form-control third"]:required'
        )
        input_email.send_keys("nn@mailto.plus")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_element = WebDriverWait(browser, 15).until(
            ec.presence_of_element_located((By.TAG_NAME, "h1"))
        )

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
