"""#6"""

from typing import (
    List,
    Tuple,
    Union,
    Optional,
    TypeVar,
    Callable
)


# #1
def calculate_discount(price: float, discount: float) -> float:
    """Обчислює ціну зі знижкою."""
    if not isinstance(price, float):
        raise TypeError("'price' має бути 'float'")
    if not isinstance(discount, float):
        raise TypeError("'discount' має бути 'float'")
    if price <= 0:
        raise ValueError("'price' має бути більше нуля")
    if 0 > discount:
        raise ValueError("'discount' має дорівнювати або бути вище за нуль")

    if discount > 100:
        return 0.0

    return price * (1 - discount / 100)


# #2
def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Фільтрує список людей, залишаючи тільки тих, хто досяг повноліття."""
    if not isinstance(people, list):
        raise TypeError("'people' має бути списком")
    if not people:
        raise TypeError("'people' не може бути порожнім списком")

    for person in people:
        if not isinstance(person, tuple):
            raise TypeError("елементи 'people' мають бути кортежами")
        if not isinstance(person[0], str) or not isinstance(person[1], int):
            raise TypeError(
                "кортежі 'people' повинні вміщати ім'я(str) на першій позиції і вік(int) на другій"
            )
        if person[1] < 0:
            raise ValueError("вік не може бути менше нуля")

    return [person for person in people if person[1] >= 18]


# #3
def parse_input(value: Union[int, str]) -> Optional[int]:
    """Перетворює вхідне значення на ціле число, якщо це можливо."""
    if isinstance(value, int):
        return value

    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None

    return None


# #4
T = TypeVar("T")

def get_first(lst: List[T]) -> Optional[T]:
    """Повертає перший елемент списку або None, якщо список порожній."""
    return lst[0] if lst else None


# #5
def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    """Застосовує задану операцію до числа."""
    return operation(x)

def square(n: int) -> int:
    return n * n

def double(n: int) -> int:
    return n * 2
