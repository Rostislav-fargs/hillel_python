class CustomCltnFunc:
    """Клас для демонстрації власних версій функцій len(), sum() та min()."""

    def __init__(self, data: list):
        """
        Ініціалізація колекції.

        Arguments:
            data (list): Список елементів для зберігання в колекції.
        """
        self.data = data

    def __len__(self):
        """
        Реалізація власної версії функції len().

        Returns:
            int: Кількість елементів у колекції.
        """
        count = 0
        for i in self.data:
            count += 1
        return count

    def __iter__(self):
        """
        Реалізація власної версії ітератора для колекції.

        Returns:
            iterator: Ітератор для проходження через елементи колекції.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Повертає наступний елемент у колекції.

        Returns:
            element: Наступний елемент у колекції.

        Raises:
            StopIteration: Якщо всі елементи колекції були відвідані.
        """
        if self._index < len(self.data):
            result = self.data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        """
        Доступ до елементів за індексом.

        Arguments:
            index (int): Індекс елемента.

        Returns:
            element: Елемент колекції за індексом.
        """
        return self.data[index]

    def __iter__(self):
        """Потрібно перезаписати метод __iter__."""
        self._index = 0
        return self


def my_len(obj):
    """
    Реалізація власної функції len().
    """
    return obj.__len__()

def my_sum(obj):
    """
    Реалізація власної функції sum().
    """
    total = 0
    for item in obj:
        total += item
    return total

def my_min(obj):
    """
    Реалізація власної функції min().
    """
    if not obj:
        raise ValueError("min() arg is an empty collection")

    min_value = obj[0]
    for item in obj:
        if item < min_value:
            min_value = item
    return min_value


# Тестування

if __name__ == "__main__":
    collection = CustomCltnFunc([3, 5, 1, 9, 2])

    print(f"Довжина колекції: {my_len(collection)}")  # 5
    print(f"Сума елементів колекції: {my_sum(collection)}")  # 20
    print(f"Мінімальний елемент колекції: {my_min(collection)}")  # 1
