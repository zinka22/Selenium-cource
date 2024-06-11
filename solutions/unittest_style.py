# Задание содержится в tasks/unittest_style.md

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class RegistrationFormTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_check_registration_form(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        input_name = self.browser.find_element(By.CLASS_NAME, "form-control.first")
        input_name.send_keys("Ivan")
        input_surname = self.browser.find_element(By.CLASS_NAME, "form-control.second")
        input_surname.send_keys("Petrov")
        input_email = self.browser.find_element(By.CLASS_NAME, "form-control.third")
        input_email.send_keys("nn@mailto.plus")

        submit_button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        submit_button.click()

        welcome_text_element = WebDriverWait(self.browser, 15).until(
            ec.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        welcome_text = welcome_text_element.text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Welcome text should be 'Congratulations! You have successfully registered!'",
        )

    def test_check_registration_with_bugs(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        input_name = self.browser.find_element(
            By.CSS_SELECTOR, '[class="form-control first"]:required'
        )
        input_name.send_keys("Ivan")
        input_surname = self.browser.find_element(
            By.CSS_SELECTOR, '[class="form-control second"]:required'
        )
        input_surname.send_keys("Petrov")
        input_email = self.browser.find_element(
            By.CSS_SELECTOR, '[class="form-control third"]:required'
        )
        input_email.send_keys("nn@mailto.plus")

        submit_button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        submit_button.click()

        welcome_text_element = WebDriverWait(self.browser, 15).until(
            ec.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        welcome_text = welcome_text_element.text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Welcome text should be 'Congratulations! You have successfully registered!'",
        )


if __name__ == "__main__":
    unittest.main()
