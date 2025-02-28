"""#5"""

import pytest


def divide(a: int | float, b: int | float) -> float:
    """
    Функція для ділення двох чисел.

    Arguments:
        a (int | float): Число, яке буде поділено.
        b (int | float): Число, на яке буде виконано ділення.

    Returns:
        float: Результат ділення числа a на число b.

    Raises:
        TypeError: Якщо аргументи не є числами (int або float).
        ZeroDivisionError: Якщо аргумент b дорівнює нулю.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be 'int' or 'float'")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be 'int' or 'float'")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


# Тест для коректного ділення
def test_divide_correct():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(1, 1) == 1.0


# Тест для перевірки винятку ZeroDivisionError
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)


# Тест на неправильнйи тип даних для a
def test_divide_by_wrong_type_a():
    with pytest.raises(TypeError, match="'a' must be 'int' or 'float'"):
        divide('10', 2)


# Тест на неправильнйи тип даних для b
def test_divide_by_wrong_type_b():
    with pytest.raises(TypeError, match="'b' must be 'int' or 'float'"):
        divide(10, '2')


# Тест з параметризацією для перевірки ділення з різними значеннями
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (1, 1, 1.0),
    (20, 5, 4.0),
    (100, 25, 4.0)
])
def test_divide_parametrized(a, b, expected):
    result = divide(a, b)
    assert result == expected
