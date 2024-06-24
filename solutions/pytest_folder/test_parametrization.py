# Задание содержится в tasks/test_parametrization.md

import math
import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

urls = [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905",
]


@pytest.mark.parametrize("link", urls)
def test_check_urls_on_feedback(browser, auth_data, link):
    # авторизация
    browser.get(f"https://stepik.org/lesson/{link}/step/1")

    enter_button = browser.find_element(By.CLASS_NAME, "navbar__auth_login ")
    enter_button.click()

    input_login = browser.find_element(By.ID, "id_login_email")
    input_login.send_keys(auth_data["login"])

    input_password = browser.find_element(By.ID, "id_login_password")
    input_password.send_keys(auth_data["password"])

    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit_button.click()

    def user_is_authorised():
        """Check if user was authorized"""
        try:
            popup_is_closed = WebDriverWait(browser, 5).until(
                ec.invisibility_of_element_located((By.ID, "login_form"))
            )
            return popup_is_closed
        except TimeoutException:
            return False

    if user_is_authorised():

        # проверяем, есть ли кнопка "Решить снова"
        try:
            again_button = WebDriverWait(browser, 15).until(
                ec.element_to_be_clickable((By.CLASS_NAME, "again-btn"))
            )
            if again_button:
                again_button.click()
        except TimeoutException:
            pass

        # решаем, отправляем решение
        input_answer = WebDriverWait(browser, 120).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
        )
        input_answer.send_keys(str(math.log(int(time.time()))))

        send_answer_button = WebDriverWait(browser, 120).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        send_answer_button.click()

        # проверяем, совпадает ли текст с ожидаемым
        feedback_text = (
            WebDriverWait(browser, 150)
            .until(ec.visibility_of_element_located((By.CLASS_NAME, "smart-hints")))
            .text
        )

        assert feedback_text == "Correct!", f"Wait {'Correct!'} got {feedback_text}"
    else:
        assert user_is_authorised(), "User is guest"
