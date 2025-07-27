from src.decorators import log
import os


# Простая функция для тестирования успешного выполнения
@log()
def add(a, b):
    return a + b


# Функция, которая всегда вызывает ошибку
@log()
def bad_func():
    raise ValueError("Something went wrong")


# Тест 1: Проверяем, что декоратор не ломает работу функции
def test_function_works():
    result = add(2, 3)
    assert result == 5


# Тест 2: Проверяем вывод в консоль при успешном выполнении
def test_log_output_success(capsys):
    add(1, 2)
    captured = capsys.readouterr()
    output = captured.out

    # Проверяем что вывод содержит нужные части
    assert "add ok" in output
    assert "error" not in output


# Тест 3: Проверяем вывод ошибки в консоль
def test_log_output_error(capsys):
    try:
        bad_func()
    except ValueError:
        pass

    captured = capsys.readouterr()
    output = captured.out

    assert "bad_func error" in output
    assert "ValueError" in output


# Тест 4: Проверяем запись в файл
def test_log_to_file():
    test_filename = "test_log.txt"

    # Удаляем файл если он уже есть
    if os.path.exists(test_filename):
        os.remove(test_filename)

    # Создаем функцию с записью в файл
    @log(filename=test_filename)
    def test_func(x):
        return x * 2

    test_func(5)  # Вызываем функцию

    # Проверяем что файл создан и содержит нужную запись
    assert os.path.exists(test_filename)
    with open(test_filename) as f:
        content = f.read()
        assert "test_func ok" in content

    # Удаляем тестовый файл после проверки
    os.remove(test_filename)
