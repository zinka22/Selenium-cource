from base_page import BasePage
from locators import ProductPageLocators
import re


class ProductPage(BasePage):
    def should_be_able_to_add_product_to_basket(self):
        self.should_be_product_url()
        self.should_add_product_to_cart()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert re.search(
            r"catalogue/.+", current_url
        ), f"Expected URL to contain the word 'catalogue' and product name, but got '{current_url}'."

    def should_add_product_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        assert button_add_to_cart, "Add to basket button is absent"

        button_add_to_cart.click()
