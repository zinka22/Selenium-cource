from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = None

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element(By.CSS_SELECTOR, "#num1")
    first = first_number.text
    second_number = browser.find_element(By.CSS_SELECTOR, "#num2")
    second = second_number.text
    math_result = str(int(first) + int(second))

    select_element = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select_element.select_by_value(value=str(math_result))

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()




