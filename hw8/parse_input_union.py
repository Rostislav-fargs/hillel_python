"""#3"""

from typing import Union, Optional


def parse_input(value: Union[int, str]) -> Optional[int]:
    """
    Перетворює вхідне значення на ціле число, якщо це можливо.

    Argumetns:
        value (Union[int, str]): Вхідне значення, яке може бути цілим числом або рядком.

    Returns:
        Optional[int]: Ціле число, якщо конвертація можлива, або None в іншому випадку.
    """
    if isinstance(value, int):
        return value

    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            pass

    return None


if __name__ == "__main__":
    # Приклади використання
    print(parse_input(42))       # 42
    print(parse_input("100"))    # 100
    print(parse_input("hello"))  # None
