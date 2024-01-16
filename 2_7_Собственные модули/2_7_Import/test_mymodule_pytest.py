# pip install pytest

from mymodule import add, subtract

def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


# Обратите внимание, что структура файлов тестов и синтаксис проверок отличается от unittest.
# Для pytest вам просто нужно определить функции тестов с префиксом test_,
# а затем добавить проверки с использованием оператора assert.
# Обе библиотеки позволяют вам автоматизировать тестирование ваших модулей и убедиться,
# что ваш код функционирует корректно. Выбор между unittest и pytest зависит
# от ваших личных предпочтений и требований проекта.