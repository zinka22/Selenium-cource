from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
    page.is_element_present(*ProductPageLocators.ADD_TO_CART)
    page.should_be_able_to_add_product_to_basket()
    page.solve_quiz_and_get_code()
