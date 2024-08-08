from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "id_login-username")
    REGISTER_FORM = (By.ID, "id_registration-email")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CLASS_NAME, "product_main h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
