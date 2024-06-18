## Задание к [test_authorization](../solutions/pytest_folder/test_authorization.py)

### Авторизация на сайте

Вам необходимо авторизоваться на stepik со своим логином и паролем. Пожалуйста, будьте внимательны
и не добавляйте свои логин и пароль в публичные репозитории на GitHub.

Задача — реализовать автотест для запуска средствами pytest со следующим набором действий:

1) открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1;
2) авторизоваться со своими логином и паролем;
3) дождаться того, что поп-апа с авторизацией больше нет.

Для запуска теста на локальной машине:

1) в файле auth_keys_stepik.json заменить тестовые логин и пароль на свои данные, актуальные для авторизации;
2) запустить тест в терминале при помощи команды pytest <путь к файлу> или в PyCharm с использованием Run.