from time import sleep

from selenium.webdriver.common.by import By


def test_run_for_different_locals(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    sleep(30)
    add_to_basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")

    assert add_to_basket_button, "Add to basket button is absent"
