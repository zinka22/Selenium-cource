## Задание к [expected_conditions](../solutions/expected_conditions.py)

### Настройка ожиданий

Попробуем теперь написать программу, которая будет бронировать нам дом
для отдыха по строго заданной цене. Более высокая цена нас не устраивает,
а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять
следующий сценарий:

1) открыть страницу http://suninjuly.github.io/explicit_wait2.html;
2) дождаться, когда цена дома уменьшится до $100 (ожидание нужно
   установить не меньше 12 секунд);
3) нажать на кнопку "Book";
4) решить уже известную нам математическую задачу (используйте ранее
   написанный код) и отправить решение;
5) чтобы определить момент, когда цена аренды уменьшится до $100,
   используйте метод text_to_be_present_in_element из библиотеки
   expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом.
Отправьте его в качестве ответа на это задание.