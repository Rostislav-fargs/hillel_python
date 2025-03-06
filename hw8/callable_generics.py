"""#8"""

from typing import List, Callable, TypeVar


# Тип T для узагальнених параметрів
T = TypeVar('T')


class Processor:
    """
    Клас для обробки даних за допомогою функцій, що застосовуються до елементів списку.
    
    Attributes:
        data (List[T]): Список даних для обробки.
    """
    def __init__(self, data: List[T]) -> None:
        self.data = data

    def apply(self, func: Callable[[T], T]) -> List[T]:
        """
        Застосовує функцію до кожного елемента списку.

        Arguments:
            func (Callable[[T], T]): Функція, яку потрібно застосувати до кожного елемента.

        Returns:
            List[T]: Список результатів застосування функції до кожного елемента.
        """
        return [func(item) for item in self.data]


if __name__ == "__main__":
    # Функція для подвоєння числа
    def double(x: int) -> int:
        """Подвоює число."""
        return x * 2

    # Функція для перетворення рядка в верхній регістр
    def to_upper(s: str) -> str:
        """Перетворює рядок у верхній регістр."""
        return s.upper()

    # Приклад для чисел
    p1 = Processor([1, 2, 3])
    print(p1.apply(lambda x: x * 2))  # [2, 4, 6]

    # Приклад для рядків
    p2 = Processor(["hello", "world"])
    print(p2.apply(str.upper))  # ["HELLO", "WORLD"]

    # Альтернативне використання функцій double та to_upper
    p3 = Processor([1, 2, 3])
    print(p3.apply(double))  # [2, 4, 6]

    p4 = Processor(["hello", "world"])
    print(p4.apply(to_upper))  # ["HELLO", "WORLD"]
