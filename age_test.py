"""#9"""

import pytest


class AgeVerifier:
    """Клас для перевірки віку користувачів."""

    @staticmethod
    def verification(age: int) -> bool:
        """Перевіряє, чи є користувач повнолітнім.

        Args:
            age (int): Вік користувача.

        Returns:
            bool: True, якщо вік більше або дорівнює 18, інакше False.

        Raises:
            TypeError: Якщо `age` не є цілим числом.
            ValueError: Якщо `age` є від'ємним числом.
        """
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age >= 18


@pytest.mark.parametrize("age", [18, 17, 20, 121, 150, -5])
def test_verification(age):
    if age > 120:
        pytest.skip("Неправильне значення віку")

    if age < 0:
        pytest.skip("Негативний вік — тест пропущено.")

    assert AgeVerifier.verification(age) == (age >= 18)
