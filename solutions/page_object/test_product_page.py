# Задание содержится в tasks/test_product_page.md
# Задание к негативным тестам содержится в tasks/task_negative_tests.md
# Задание для класса TestUserAddToBasketFromProductPage (запуск с -m login_guest) в tasks/task_grouping_and_setup.md

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

base_shop_url = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
shop_url_for_login = (
    "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
)

login_page_url = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url)
    page.open()
    page.should_be_able_to_add_product_to_cart()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_in_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_shop_url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_shop_url)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_element_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, shop_url_for_login)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, shop_url_for_login)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.login_guest_v
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_page_url)
        page.open()
        page.should_be_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, base_shop_url)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, base_shop_url)
        page.open()
        page.should_be_able_to_add_product_to_cart()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_in_cart()
