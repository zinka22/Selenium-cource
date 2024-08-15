# Задание содержится в tasks/test_product_page.md
# Задание к негативным тестам содержится в tasks/task_negative_tests.md

import pytest

from conftest import base_shop_url
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url)
    page.open()
    page.should_be_able_to_add_product_to_cart()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_in_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url, timeout=0)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_shop_url, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url, timeout=0)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_element_disappear()
