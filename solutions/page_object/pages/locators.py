from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    CONFIRM_REGISTRATION = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.ID, "id_login-username")
    PASSWORD_FORM = (By.ID, "id_registration-password1")
    REGISTER_FORM = (By.ID, "id_registration-email")
    SUCCESS_REGISTER = (By.CLASS_NAME, "alertinner")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CLASS_NAME, "product_main h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
