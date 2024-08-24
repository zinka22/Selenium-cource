## Задание к [test_product_page.py](../solutions/page_object/test_product_page.py)

### Плюсы наследования: пример

В предыдущем уроке мы написали тест "Гость может перейти на страницу логина с главной страницы магазина". Но если вы
внимательно посмотрите на остальные страницы, то заметите, что ссылка на страницу логина присутствует на каждой
странице. Если мы хотим добавить тест "гость может перейти на страницу логина со страницы товара", то для избежания
дублирования, логично перенести соответствующие методы в класс BasePage. Давайте так и поступим:

В файле locators.py создаем новый класс BasePageLocators и переносим туда соответствующие элементы:

```
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
```

В файл base_page.py переносим соответствующие методы, заменяя класс с локаторами на BasePageLocators:

```
from .locators import BasePageLocators

class BasePage():
...
    def go_to_login_page(self):
    link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
    link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
```

Примечание: методы лучше всего описывать в классе в алфавитном порядке, так проще ориентироваться и находить.

В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку:

```
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
    super(MainPage, self).__init__(*args, **kwargs)
```

Как вы уже знаете, метод `__init__` вызывается при создании объекта. Конструктор выше с ключевым словом `super` на самом
деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор
MainPage.

Теперь мы можем легко добавлять тесты вида "Гость может перейти на страницу логина со страницы Х".

Добавляем в файл c тестами test_product_page.py новые тесты:

```
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
```

Добавьте самостоятельно второй тест `test_guest_can_go_to_login_page_from_product_page`. Запустите тесты и убедитесь,
что они проходят.
