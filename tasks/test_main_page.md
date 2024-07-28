## Задание для [test_main_page](../solutions/page_object/test_main_page.py)

### Обучающее задание: test_main_page

1) Создайте файл test_main_page.py и добавьте в него тест:

       def test_guest_can_go_to_login_page(browser):
           link = "http://selenium1py.pythonanywhere.com/"
           browser.get(link)
           login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
           login_link.click()

2) Выделите открытие страницы логина в отдельный метод:

       def go_to_login_page(browser):
           login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
           login_link.click()

   Тест стал проще:

       def test_guest_can_go_to_login_page(browser): 
           browser.get(link) 
           go_to_login_page(browser) 

3) Базовая страница для проекта: BasePage

   Перепишем тест из файла test_main_page.py с помощью паттерна Page Object. Будем работать с главной страницей
   нашего приложения, поэтому дадим классу говорящее название MainPage.

    1. Создайте в своём проекте папку pages, там мы будем хранить все наши Page Object.
    2. В папке создайте два файла: base_page.py и main_page.py.
       Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем
       вспомогательные методы для работы с драйвером.
    3. В файле base_page.py создайте класс с названием BasePage.
       В Python такие вещи делаются с помощью следующей конструкции: `class BasePage():`
    4. Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод, который вызывается, когда мы
       создаём объект. Конструктор объявляется ключевым словом `__init__`. В него в качестве параметров мы передаём
       экземпляр драйвера и URL. Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. Получается
       примерно так:

           def __init__(self, browser, url):
               self.browser = browser
               self.url = url

    5. Теперь добавим ещё один метод `open`. Он должен открывать нужную страницу в браузере, используя метод `get()`.
       Объявите ниже в том же классе: `def open(self):` и реализуйте этот метод: нужна всего одна строка.
    6. В итоге у вас должен быть следующий код в файле base_page.py:

           class BasePage():
               def __init__(self, browser, url):
                   self.browser = browser
                   self.url = url

               def open(self):
                   # ваша реализация

4) Page Object для главной страницы сайта

   Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина.

    1. Откройте файл main_page.py.
    2. В нём нужно сделать импорт базового класса BasePage: `from .base_page import BasePage`.
    3. В нём создайте класс MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в
       скобках: `class MainPage(BasePage):`, таким образом, класс MainPage будет иметь доступ ко всем атрибутам и
       методам своего класса-предка.
    4. Перенесите метод из предыдущего урока в класс MainPage:

           def go_to_login_page(browser):
               login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
               login_link.click() 

   Чтобы всё работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера, мы его
   передаём и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент `self`, чтобы иметь доступ к
   атрибутам и методам класса: `def go_to_login_page(self):`. Так как браузер у нас хранится как аргумент класса
   BasePage, обращаться к нему нужно соответствующим образом с помощью `self`:
   `self.browser.find_element(By.CSS_SELECTOR, "#login_link")`. В итоге файл main_page.py будет выглядеть так:

           from .base_page import BasePage
           from selenium.webdriver.common.by import By


           class MainPage(BasePage):
               def go_to_login_page(self):
                   login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
                   login_link.click()

5) Первый тест на основе Page Object

    1. Откройте файл с вашим тестом test_main_page.py.
    2. В самом верху файла нужно импортировать класс, описывающий главную страницу:
       `from .pages.main_page import MainPage`.
    3. Теперь преобразуем сам тест в test_main_page.py:

           from .pages.main_page import MainPage


           def test_guest_can_go_to_login_page(browser):
               link = "http://selenium1py.pythonanywhere.com/"
               page = MainPage(browser, link)   # инициализируем Page Object, передаём в конструктор
                                                # экземпляр драйвера и url адрес
               page.open()                      # открываем страницу
               page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    4. Убедитесь, что тест проходит, запустив его командой:
       `pytest -v --tb=line --language=en test_main_page.py`

6) Методы-проверки в Page Object

   Давайте теперь автоматизируем другой тест-кейс и посмотрим на его примере, как делать методы-проверки. Допустим, нам
   нужно проверять такой сценарий:

    * Открыть главную страницу.
    * Проверить, что есть ссылка, которая ведёт на логин. Для этого в классе MainPage нужно реализовать метод, который
      будет проверять наличие ссылки. Обычно все такие методы-проверки называются похожим образом, мы будем называть их
      should_be_(название элемента). Итак, в классе MainPage создайте метод `should_be_login_link`. Для первой пробы
      можно реализовать его самым примитивным образом:

          def should_be_login_link(self):
              self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

   Сейчас мы намеренно сделали селектор неправильным, чтобы посмотреть, что именно выдаст тест, если поймает баг. Это
   хорошая практика: писать сначала красные тесты и только потом делать их зелёными.

   Добавляем в файл с тест-кейсами новый тест:

          def test_guest_should_see_login_link(browser):
              link = "http://selenium1py.pythonanywhere.com/"
              page = MainPage(browser, link)
              page.open()
              page.should_be_login_link()

7) Проверка элемента на странице

   Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и перехватывать
   исключения.

   Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать
   нам `True` или `False`. Можно сделать это по-разному (с настройкой явных или неявных ожиданий). Сейчас воспользуемся
   неявным ожиданием.

    1. В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:

           def __init__(self, browser, url, timeout=10):
               self.browser = browser
               self.url = url
               self.browser.implicitly_wait(timeout)

    2. Теперь в этом же классе реализуем метод `is_element_present`, в котором будем перехватывать исключение. В него
       будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).

       Чтобы перехватывать исключение, нужна конструкция try/except:

           def is_element_present(self, how, what):
               try:
                   self.browser.find_element(how, what)
               except (имя исключения):
                   return False
               return True

       Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
       `from selenium.common.exceptions import имя_исключения`. Отлично! Теперь для всех проверок, что элемент
       действительно присутствует на странице, мы можем использовать этот метод.

    3. Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:

           def should_be_login_link(self):
               assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

8) Элементы страниц в паттерне Page Object

   Представим себе ситуацию, что у нас модный быстрый agile: разработчики постоянно вносят изменения в продукт. В
   какой-то прекрасный момент изменения коснулись и шапки сайта. Вот приходит к вам разработчик с новой ссылкой и
   говорит протестировать. Замените линк, на котором запускаются тесты на
   http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer.
   Запустите тесты командой: `pytest -v --tb=line --language=en test_main_page.py`. Тесты упали, и теперь нам нужно
   их поддерживать, то есть чинить. Подберите новый селектор к ссылке на логин. Нам придётся поправить в файле
   main_page.py несколько мест, где используется изменённый селектор. Чтобы этого избежать, при проектировании тестов
   (да и вообще кода) хорошей практикой является выносить селектор во внешнюю переменную. Давайте этим и займемся:

    1. В папке pages создайте новый файл locators.py.
    2. Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject, каждый селектор — это
       пара: как искать и что искать:

           from selenium.webdriver.common.by import By


           class MainPageLocators():
               LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    3. В файле main_page.py импортируйте новый класс с локаторами: `from .locators import MainPageLocators`.
    4. Теперь в классе MainPage замените все строки, где содержится `#login_link` таким образом:

           def should_be_login_link(self):
               assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

   Обратите внимание здесь на символ `*` — он указывает на то, что мы передали именно пару, и этот кортеж нужно
   распаковать.

9) Реализация LoginPage

   Проверим, что мы действительно перешли на страницу логина. Для этого нам будет нужен новый Page Object. Заодно
   разберёмся, как между ними переключаться в ходе теста. Добавьте шаблон для LoginPage его в папку pages.

       from .base_page import BasePage


       class LoginPage(BasePage):
           def should_be_login_page(self):
               self.should_be_login_url()
               self.should_be_login_form()
               self.should_be_register_form()

           def should_be_login_url(self):
               # реализуйте проверку на корректный url адрес
               assert True

           def should_be_login_form(self):
               # реализуйте проверку, что есть форма логина
               assert True

           def should_be_register_form(self):
               # реализуйте проверку, что есть форма регистрации на странице
               assert True

   Внутри есть заглушки для методов проверок:

       should_be_login_url
       should_be_login_form
       should_be_register_form

   Реализуйте их самостоятельно:

    1. В файле locators.py создайте класс LoginPageLocators.
    2. Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators.
    3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке.
       Напишите сначала красный тест, чтобы убедиться в понятности вывода.
    4. В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем URL браузера. Для этого
       используйте соответствующее свойство Webdriver.

10) Переходы между страницами

    Инициализируем LoginPage в теле теста (не забудьте импортировать в файл нужный класс):

        from .pages.login_page import LoginPage


        def test_guest_can_go_to_login_page(browser):
            link = "http://selenium1py.pythonanywhere.com"
            page = MainPage(browser, link)
            page.open()
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            login_page.should_be_login_page()
