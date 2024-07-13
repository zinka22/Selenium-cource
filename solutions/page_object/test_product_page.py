# Задание содержится в tasks/test_product_page.md

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_product_to_cart()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_in_cart()
