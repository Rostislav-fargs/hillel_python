from math import gcd


class Fraction:
    """Клас для роботи з дробами."""

    def __init__(self, numerator: int | float, denominator: int | float):
        """
        Ініціалізація дробу.

        Перевірка, чи знаменник не дорівнює нулю.
        Спрощення дробу через знаходження НСД.

        Arguments:
            numerator (int | float): Чисельник дробу.
            denominator (int | float): Знаменник дробу.

        Raises:
            ValueError: Якщо знаменник дорівнює нулю.
        """
        if denominator == 0:
            raise ValueError("Dominator cannot be zero")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common


    def __add__(self, other):
        """
        Додавання двох дробів.

        Arguments:
            other (Fraction): Інший об'єкт класу Fraction.

        Returns:
            Fraction: Новий об'єкт класу Fraction, що є сумою двох дробів.
        """
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Віднімання двох дробів.

        Arguments:
            other (Fraction): Інший об'єкт класу Fraction.

        Returns:
            Fraction: Новий об'єкт класу Fraction, що є різницею двох дробів.
        """
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Множення двох дробів.

        Arguments:
            other (Fraction): Інший об'єкт класу Fraction.

        Returns:
            Fraction: Новий об'єкт класу Fraction, що є добутком двох дробів.
        """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """
        Ділення двох дробів.

        Arguments:
            other (Fraction): Інший об'єкт класу Fraction.

        Returns:
            Fraction: Новий об'єкт класу Fraction, що є часткою двох дробів.
        """
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __repr__(self):
        """
        Повертає рядкове подання дробу.

        Returns:
            str: Строка у форматі "чисельник/знаменник".
        """
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    obj1 = Fraction(3, 5)
    obj2 = Fraction(12, 4)

    print(f"obj1 + obj2 = {obj1} + {obj2} = {obj1 + obj2}") # obj1 + obj2 = 3/5 + 3/1 = 18/5
    print(f"obj1 - obj2 = {obj1} - {obj2} = {obj1 - obj2}") # obj1 - obj2 = 3/5 - 3/1 = -12/5
    print(f"obj1 * obj2 = {obj1} * {obj2} = {obj1 * obj2}") # obj1 * obj2 = 3/5 * 3/1 = 9/5
    print(f"obj1 / obj2 = {obj1} / {obj2} = {obj1 / obj2}") # obj1 / obj2 = 3/5 / 3/1 = 1/5
