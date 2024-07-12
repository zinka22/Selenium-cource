from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
    page.should_button_add_to_cart_present()
    page.should_be_able_to_add_product_to_basket()
    page.solve_quiz_and_get_code()
