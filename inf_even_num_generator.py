"""#5"""

from typing import Generator


def even_numbers() -> Generator[int, None, None]:
    """
    Генератор, що генерує нескінченну послідовність парних чисел.
    
    Yields:
        int: Наступне парне число.
    """
    number = 0
    while True:
        yield number
        number += 2


class LimitedGenerator:
    """Менеджер контексту, що обмежує кількість ітерацій генератора."""

    def __init__(self, generator: Generator[int], limit: int) -> None:
        """
        Ініціалізує менеджер контексту з обмеженням на кількість ітерацій.

        Arguments:
            generator (Generator[int]): Генератор для обробки.
            limit (int): Ліміт кількості елементів, які генеруються.
        """
        self.generator = generator
        self.limit = limit
        self.count = 0


    def __enter__(self) -> "LimitedGenerator":
        """Ініціалізує ітератор генератора."""
        self.iterator = iter(self.generator)
        return self


    def __iter__(self) -> "LimitedGenerator":
        """Повертає ітератор."""
        return self


    def __next__(self) -> int:
        """
        Повертає наступне значення генератора.

        Returns:
            int: Наступне парне число.
        
        Raises:
            StopIteration: Якщо ліміт досягнуто.
        """
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return next(self.iterator)


    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Закриває менеджер."""
        pass


if __name__ == "__main__":
    OUTPUT_FILE = "even_numbers.txt"
    with LimitedGenerator(even_numbers(), 200) as gen, open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for num in gen:
            file.write(str(num) + "\n")
