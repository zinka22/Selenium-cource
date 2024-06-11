## Задание к [check_registration_with_bugs](../check_registration_with_bugs.py)

### Уникальность селекторов: NoSuchElementException

Сценарий для реализации выглядит так:

1) открыть страницу https://suninjuly.github.io/registration2.html;
2) пройти регистрацию аналогично задаче [check_registration_form](check_registration_form.md);
3) закрыть браузер.

Если тест падает с ошибкой NoSuchElementException, задание выполнено правильно.
Если форма успешно заполнена и отправлена, проверьте уникальность селекторов: тест
пропустил серьезный баг.
