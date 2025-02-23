import math


class Vector:
    """Клас, що представляє вектор у просторі з n вимірами."""

    def __init__(self, *coordinates):
        """
        Ініціалізація вектора.

        Arguments:
            *coordinates (float): Координати вектора.
        """
        self._coordinates = tuple(coordinates)

    @property
    def coordinates(self):
        """Повертає координати вектора."""
        return self._coordinates

    @property
    def magnitude(self):
        """
        Обчислює довжину (модуль) вектора.

        Returns:
            float: Довжина вектора.
        """
        return math.sqrt(sum(x**2 for x in self._coordinates))

    def __add__(self, other):
        """
        Додавання двох векторів.

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            Vector: Новий вектор, що є сумою двох векторів.

        Raises:
            ValueError: Якщо вектори мають різну кількість координат.
        """
        if len(self._coordinates) != len(other._coordinates):
            raise ValueError("Вектори повинні мати однакову розмірність")
        return Vector(*(a + b for a, b in zip(self._coordinates, other._coordinates)))

    def __sub__(self, other):
        """
        Віднімання двох векторів.

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            Vector: Новий вектор, що є різницею двох векторів.

        Raises:
            ValueError: Якщо вектори мають різну кількість координат.
        """
        if len(self._coordinates) != len(other._coordinates):
            raise ValueError("Вектори повинні мати однакову розмірність")
        return Vector(*(a - b for a, b in zip(self._coordinates, other._coordinates)))

    def __mul__(self, other):
        """
        Обчислення скалярного добутку двох векторів.

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            float: Скалярний добуток векторів.

        Raises:
            ValueError: Якщо вектори мають різну кількість координат.
        """
        if len(self._coordinates) != len(other._coordinates):
            raise ValueError("Вектори повинні мати однакову розмірність")
        return sum(a * b for a, b in zip(self._coordinates, other._coordinates))

    def __lt__(self, other):
        """Менше за довжиною."""
        return self.magnitude < other.magnitude

    def __eq__(self, other):
        """Перевірка на рівність довжин векторів."""
        return math.isclose(self.magnitude, other.magnitude, rel_tol=1e-9)

    def __repr__(self):
        """Повертає строкове представлення вектора."""
        return f"Vector{self._coordinates}"


# Тестування
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(1, 2, 3)

    print(f"v1: {v1}, v2: {v2}")
    print(f"Довжина v1: {v1.magnitude}")
    print(f"Довжина v2: {v2.magnitude}")
    print(f"Сума v1 + v2: {v1 + v2}")
    print(f"Різниця v1 - v2: {v1 - v2}")
    print(f"Скалярний добуток v1 * v2: {v1 * v2}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"v1 == v3: {v1 == v3}")

    # v1: Vector(1, 2, 3), v2: Vector(4, 5, 6)
    # Довжина v1: 3.7416573867739413
    # Довжина v2: 8.774964387392123
    # Сума v1 + v2: Vector(5, 7, 9)
    # Різниця v1 - v2: Vector(-3, -3, -3)
    # Скалярний добуток v1 * v2: 32
    # v1 < v2: True
    # v1 == v3: True
