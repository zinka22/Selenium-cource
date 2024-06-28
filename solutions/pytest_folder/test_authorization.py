# Задание содержится в tasks/test_authorization.md

from selenium.webdriver.common.by import By

from helpers import assert_if_user_is_authorized_on_lesson_page


def test_authorization(browser, auth_data):
    browser.get("https://stepik.org/lesson/236895/step/1")

    enter_button = browser.find_element(By.ID, "ember459")
    enter_button.click()

    input_login = browser.find_element(By.ID, "id_login_email")
    input_login.send_keys(auth_data["login"])

    input_password = browser.find_element(By.ID, "id_login_password")
    input_password.send_keys(auth_data["password"])

    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit_button.click()

    assert_if_user_is_authorized_on_lesson_page(browser)
