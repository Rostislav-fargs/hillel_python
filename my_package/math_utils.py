"""
math_utils.py

Модуль для роботи з рядками.

Містить функції:
    factorial: Повертає факторіал наданого натурального числа.
    my_gcd: Повертає найбільший спільний дільник двох цілих чисел.
"""


def factorial(number: int) -> int:
    """
    Обраховує і повертає факторіал числа number.

    Arguments:
        number (int): Число для розрахунку факторіалу.
            Повинне бути цілим невід'ємним числом.

    Returns:
        int: Результат розрахунку факторіалу.

    Raises:
        TypeError: Якщо передано не ціле число.
        ValueError: Якщо число менше нуля.
    """
    if not isinstance(number, int):
        raise TypeError("Очікується ціле число")
    if number < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних чисел")

    if number == 0:
        return 1
    return number * factorial(number - 1)


def my_gcd(a: int, b: int) -> int:
    """
    Обчислює найбільший спільний дільник двох чисел a і b
    за допомогою алгоритму Евкліда.

    Arguments:
        a (int): Перше число.
        b (int): Друге число.

    Returns:
        int: Найбільший спільний дільник чисел a і b.

    Raises:
        TypeError: Якщо передано нецілі числа.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Очікуються цілі числа")

    if b == 0:
        return abs(a)
    return my_gcd(b, a % b)
