import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = None

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest_element = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
    x = float(chest_element.get_attribute("valuex"))

    result_function = math.log(abs(12 * math.sin(x)))

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(result_function)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    submit_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() if browser else ...
