# Задание содержится в tasks/test_product_page.md
# Задание к негативным тестам содержится в tasks/task_negative_tests.md

import pytest

from pages.product_page import ProductPage

base_shop_url = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
implicit_wait_default_value = 0


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url)
    page.open()
    page.should_be_able_to_add_product_to_cart()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_in_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url, timeout=implicit_wait_default_value)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_shop_url, timeout=implicit_wait_default_value)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url, timeout=implicit_wait_default_value)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_element_disappear()
