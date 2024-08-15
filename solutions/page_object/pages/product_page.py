import re

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_able_to_add_product_to_cart(self):
        self.should_be_product_url()
        self.should_button_add_to_cart_present()

    def should_be_in_cart(self):
        self.should_be_right_product_name_in_success_message()
        self.should_cart_price_be_equal_product_price()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert re.search(
            r"catalogue/.+/\?promo=newYear", current_url
        ), f"Expected URL to contain the word 'catalogue' and product name, but got '{current_url}'."

    def should_button_add_to_cart_present(self):
        button_add_to_cart = self.is_element_present(ProductPageLocators.ADD_TO_CART)
        assert button_add_to_cart, "Add to basket button is absent"

    def add_product_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        assert button_add_to_cart.is_enabled(), "Button is not clickable"
        button_add_to_cart.click()

    def should_be_right_product_name_in_success_message(self):
        product_name_in_success_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE
        ).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert (
            product_name_in_success_message == product_name
        ), "Wrong item added to cart"

    def should_cart_price_be_equal_product_price(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        assert cart_price == product_price, "Cart price is not equal product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_element_disappear(self):
        assert self.is_disappeared(
            ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should disappear"

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
