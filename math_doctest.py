"""#4"""

import doctest


def factorial(n: int) -> int:
    """
    Повертає факторіал числа

    Arguments:
        n (int): Число для розрахунку факторіла.

    Return:
        int: Факторіал числа n.
    
    Raises:
        TypeError: Якщо n не int.
        ValueError: Якщо n менше нуля.

    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(-2)
    Traceback (most recent call last):
        ...
    ValueError: 'n' must be equal or greater than 0
    >>> factorial('3')
    Traceback (most recent call last):
        ...
    TypeError: 'n' must be 'int'
    """
    if not isinstance(n, int):
        raise TypeError("'n' must be 'int'")
    if n < 0:
        raise ValueError("'n' must be equal or greater than 0")
    if n == 0:
        return 1
    return n * factorial(n-1)


def is_even(n: int | float) -> bool:
    """
    Перевіряє, чи є число парним.

    Arguments:
        int (int | float): Число для перевірки на парність.
    
    Return:
        bool: True якщо парне, інакше False.

    Raises:
        TypeError: Якщо n неправильного типу.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-3)
    False
    >>> is_even(4.0)
    True
    >>> is_even('4.0')
    Traceback (most recent call last):
        ...
    TypeError: 'n' must be 'int' or 'float'
    """
    if not isinstance(n, (int, float)):
        raise TypeError("'n' must be 'int' or 'float'")
    return n % 2 == 0


if __name__ == "__main__":
    doctest.testmod(verbose=True)
