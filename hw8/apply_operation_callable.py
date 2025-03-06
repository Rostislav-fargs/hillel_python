"""#5"""

from typing import Callable


def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    """
    Застосовує задану операцію до числа.

    Arguments:
        x (int): Число, до якого застосовується операція.
        operation (Callable[[int], int]): Операція, яку потрібно застосувати.

    Returns:
        int: Результат застосування операції до числа.
    """
    return operation(x)


def square(n: int) -> int:
    """
    Підносить число до квадрату.

    Arguments:
        n (int): Число, яке потрібно піднести до квадрату.

    Returns:
        int: Число в квадраті.
    """
    return n * n


def double(n: int) -> int:
    """
    Подвоює число.

    Arguments:
        n (int): Число, яке потрібно подвоїти.

    Returns:
        int: Подвоєне число.
    """
    return n * 2


if __name__ ==  "__main__":
    print(apply_operation(5, square))  # 25
    print(apply_operation(4, double))  # 8
