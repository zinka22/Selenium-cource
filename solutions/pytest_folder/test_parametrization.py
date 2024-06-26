# Задание содержится в tasks/test_parametrization.md

import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from helpers import assert_if_user_is_authorized_on_lesson_page

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
    """Test to check feedback text after successfully solving task."""
    # авторизация
    browser.get(f"https://stepik.org/lesson/{link}/step/1")

    enter_button = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
    enter_button.click()

    input_login = browser.find_element(By.ID, "id_login_email")
    input_login.send_keys(auth_data["login"])

    input_password = browser.find_element(By.ID, "id_login_password")
    input_password.send_keys(auth_data["password"])

    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit_button.click()

    assert_if_user_is_authorized_on_lesson_page(browser)

    # проверка, есть ли кнопка "Решить снова"
    if again_buttons := browser.find_elements(By.CLASS_NAME, "again-btn"):
        again_buttons[0].click()

    # решение, отправка решения
    input_answer = WebDriverWait(browser, 120).until(
        ec.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
    )
    input_answer.send_keys(str(math.log(int(time.time()))))

    send_answer_button = WebDriverWait(browser, 120).until(
        ec.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    send_answer_button.click()

    # проверка, совпадает ли текст с ожидаемым
    feedback_text = (
        WebDriverWait(browser, 150)
        .until(ec.visibility_of_element_located((By.CLASS_NAME, "smart-hints")))
        .text
    )
    assert (
        feedback_text == "Correct!"
    ), f"Expected 'Correct!' feedback text, actual is {feedback_text}."
