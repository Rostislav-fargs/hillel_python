import re


class User:
    """Клас для представлення користувача з атрибутами first_name, last_name, email."""

    def __init__(self, first_name: str, last_name: str, email: str):
        """
        Ініціалізація користувача.

        Arguments:
            first_name (str): Ім'я користувача.
            last_name (str): Прізвище користувача.
            email (str): Email користувача.

        Raises:
            ValueError: Якщо email має неправильний формат.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  # Використовуємо сеттер для перевірки email

    @property
    def first_name(self):
        """Повертає ім'я користувача."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Встановлює ім'я користувача."""
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        self._first_name = value

    @property
    def last_name(self):
        """Повертає прізвище користувача."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Встановлює прізвище користувача."""
        if not value:
            raise ValueError("Прізвище не може бути порожнім")
        self._last_name = value

    @property
    def email(self):
        """Повертає email користувача."""
        return self._email

    @staticmethod
    def is_valid_email(email):
        """
        Перевіряє, чи email має правильний формат.

        Arguments:
            email (str): Email для перевірки.

        Returns:
            bool: True, якщо email валідний, False — якщо ні.
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    @email.setter
    def email(self, value):
        """Встановлює email, якщо він має правильний формат."""
        if not self.is_valid_email(value):
            raise ValueError("Невірний формат email")
        self._email = value

    def __repr__(self):
        """Повертає рядкове представлення користувача."""
        return f"User(first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"


# Тестування
if __name__ == "__main__":
    user = User("Іван", "Петров", "ivan.petrov@example.com")
    print(user)  # User(first_name='Іван', last_name='Петров', email='ivan.petrov@example.com')

    # Оновлення значень
    user.first_name = "Олександр"
    user.last_name = "Іванов"
    user.email = "alex.ivanov@gmail.com"
    print(user)  # \User(first_name='Олександр', last_name='Іванов', email='alex.ivanov@gmail.com')

    # Спроба встановити некоректний email
    try:
        user.email = "wrong-email"
    except ValueError as e:
        print(e)  # Невірний формат email
