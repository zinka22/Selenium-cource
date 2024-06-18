# Задание содержится в tasks/test_authorization.md

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


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

    def user_is_authorised():
        try:
            popup_is_closed = WebDriverWait(browser, 5).until(
                ec.invisibility_of_element_located((By.ID, "login_form"))
            )
            return popup_is_closed
        except TimeoutException:
            return False

    assert user_is_authorised(), "User is guest"
