from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "id_login-username")
    REGISTER_FORM = (By.ID, "id_registration-email")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
