## Задание-дополнение к [test_product_page](../solutions/page_object/test_product_page.py)

### Отрицательные проверки

Иногда в ходе написания авто-тестов возникает ситуация, когда нам нужно проверить не только присутствие элемента на
странице, но и то, что элемента на странице нет. Здесь стоит разделять две принципиально разные ситуации, в зависимости
от того, как ведёт себя веб-приложение:

1) Элемент потенциально может появиться на странице (но вообще-то не должен). Например, мы открываем страницу товара, и
   ожидаем, что там нет сообщения об успешном добавлении в корзину. Мы проверяем, что элемента нет, но при позитивном
   сценарии, когда мы добавляем товар в корзину, сообщение тоже появляется не сразу. Если при негативной проверке мы не
   добавим ожидание, а сразу выдадим результат: "True, элемента действительно нет, все хорошо", мы рискуем нарваться на
   ложно-зелёный тест. То есть можем пропустить баг.
2) Элемент присутствует на странице и должен исчезнуть со временем или в результате действий пользователя. Это может
   быть, например, удаление товара из корзины или исчезновение лоадера с загрузкой.

Почему нужно писать такие проверки с осторожностью?

Во-первых, нам приходится всегда гарантированно ждать. В первом примере нам всегда нужно ждать несколько секунд, чтобы
убедиться, что элемент не появился. Если мы используем нашу написанную функцию `is_element_present`, то тест с такой
проверкой будет ждать полные и честные 10 секунд:

```
def should_not_be_success_message(self):
    assert not self.is_element_present(ProductPageLocators.SUCCESS_MESSAGE),\
    "Success message is presented"
```

Что очень много для зелёного теста. То есть implicit_wait уже в такой ситуации не подходит, придётся использовать явное
ожидание и аккуратно подбирать условия. Время ожидания тоже придется подбирать эмпирически, путем проб, ошибок,
ложноположительных и ложноотрицательных результатов.

Во-вторых, еще одна загвоздка с отрицательными проверками в том, что они могут давать ложноположительные срабатывания,
если селектор устарел. Проверяем, что элемента с таким селектором нет, — проверка проходит, так как у элемента уже
другой селектор. Элемент есть на экране — это баг, а тест зелёный. Это плохо!

Поэтому на каждый негативный тест обязательно должен приходиться положительный тест. В одном тесте проверяем, что
элемента нет, в соседнем тесте, что элемент есть. Тогда мы сможем отслеживать актуальность селектора и не пропустим
такой баг.

Можно добавить в BasePage абстрактный метод, который проверяет, что элемент не появляется на странице в течение
заданного времени:

```
def is_not_element_present(self, locator, timeout=4):
    try:
        WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((*locator)))
    except TimeoutException:
        return True

    return False
```

Тогда его использование Page Object для страницы товара будет выглядеть так:

```
def should_not_be_success_message(self):
    assert self.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE), \
    "Success message is presented, but should not be"
```

Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией
until_not, в зависимости от того, какой результат мы ожидаем:

```
def is_disappeared(self, locator, timeout=4):
    try:
        WebDriverWait(self.browser, timeout, 1, TimeoutException).\
        until_not(ec.presence_of_element_located((*locator)))
    except TimeoutException:
    return False

    return True
```

Метод-проверка в классе про страницу товара будет выглядеть аналогично should_not_be_success_message, напишите его
самостоятельно.

___
Добавьте к себе в проект функции выше и реализуйте несколько простых тестов:

1) test_guest_cant_see_success_message_after_adding_product_to_basket:
    * открыть страницу товара;
    * добавить товар в корзину;
    * проверить, что нет сообщения об успехе с помощью is_not_element_present.
2) test_guest_cant_see_success_message:
    * открыть страницу товара;
    * проверить, что нет сообщения об успехе с помощью is_not_element_present.
3) test_message_disappeared_after_adding_product_to_basket:
    * открыть страницу товара;
    * добавить товар в корзину;
    * проверить, что нет сообщения об успехе с помощью is_disappeared.

Запустите все три теста. После того как пройдёте это задание, те тесты, которые упали, пометьте как XFail или skip.
