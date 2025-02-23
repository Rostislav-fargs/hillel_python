import math

class Vector:
    """Клас для роботи з векторами у двовимірному просторі."""

    def __init__(self, x: float, y: float):
        """
        Ініціалізація вектора.

        Arguments:
            x (float): Компонента x вектора.
            y (float): Компонента y вектора.
        """
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Додавання двох векторів.

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            Vector: Новий об'єкт класу Vector, що є сумою двох векторів.
        """
        if not isinstance(other, Vector):
            raise TypeError("Операція підтримується лише для векторів")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Віднімання двох векторів.

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            Vector: Новий об'єкт класу Vector, що є різницею двох векторів.
        """
        if not isinstance(other, Vector):
            raise TypeError("Операція підтримується лише для векторів")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector':
        """
        Множення вектора на скаляр.

        Arguments:
            scalar (float): Скалярне значення, на яке множиться вектор.

        Returns:
            Vector: Новий об'єкт класу Vector, що є результатом множення вектора на скаляр.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Операція підтримується лише для числа")
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other: 'Vector') -> bool:
        """
        Порівняння векторів за довжиною (меньший за довжиною).

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            bool: True, якщо довжина поточного вектора менша за довжину іншого вектора.
        """
        if not isinstance(other, Vector):
            raise TypeError("Операція підтримується лише для векторів")
        return self.length() < other.length()

    def __eq__(self, other: 'Vector') -> bool:
        """
        Порівняння векторів за довжиною (рівні за довжиною).

        Arguments:
            other (Vector): Інший об'єкт класу Vector.

        Returns:
            bool: True, якщо довжина поточного вектора дорівнює довжині іншого вектора.
        """
        if not isinstance(other, Vector):
            raise TypeError("Операція підтримується лише для векторів")
        return self.length() == other.length()

    def length(self) -> float:
        """
        Обчислення довжини вектора.

        Returns:
            float: Довжина вектора.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self) -> str:
        """
        Повертає строкове подання вектора.

        Returns:
            str: Строка у форматі "Vector(x, y)".
        """
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 + v2 = {v1} + {v2} = {v1 + v2}")  # Vector(4, 6)
    print(f"v1 - v2 = {v1} - {v2} = {v1 - v2}")  # Vector(2, 2)
    print(f"v1 * 2 = {v1} * 2 = {v1 * 2}")  # Vector(6, 8)
    
    print(f"v1 < v2 = {v1 < v2}")  # False
    print(f"v1 == v2 = {v1 == v2}")  # False
    
    print(f"Довжина вектора v1 = {v1.length()}")  # 5.0
    print(f"Довжина вектора of v2 = {v2.length()}")  # 2.23606797749979
