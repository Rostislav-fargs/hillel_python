"""#3"""

import pytest


class UserManager:
    """Клас для керування користувачами."""

    def __init__(self) -> None:
        """Ініціалізує менеджера."""
        self.users = {}
    

    def add_user(self, name: str, age: int) -> None:
        """
        Додає користувача до системи.

        Arguments:
            name (str): Ім'я користувача.
            age (int): Вік користувача.
        """
        self.users[name] = age
    

    def remove_user(self, name: str) -> None:
        """
        Видаляє користувача з системи.

        Arguments:
            name (str): Ім'я користувача, якого потрібно видалити.
        """
        if name in self.users:
            del self.users[name]
    

    def get_all_users(self) -> list:
        """
        Повертає список всіх користувачів.

        Returns:
            list: Список всіх користувачів у вигляді списку кортежів (ім'я, вік).
        """
        return list(self.users.items())


# Фікстура для створення об'єкту з початковими користувачами
@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    # * Розкоментувати для тесту `test_skip_condition`
    # um.add_user("Charlie", 40) 
    return um


# Тест додавання нового користувача
def test_add_user(user_manager):
    user_manager.add_user("Charlie", 40)
    assert ("Charlie", 40) in user_manager.get_all_users()


# Тест видалення користувача
def test_remove_user(user_manager):
    user_manager.remove_user("Alice")
    assert ("Alice", 30) not in user_manager.get_all_users()


# Тест отримання всіх користувачів
def test_get_all_users(user_manager):
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert ("Alice", 30) in users
    assert ("Bob", 25) in users


# Skip тесту якщо кількість користувачів менше за 3
def test_skip_condition(user_manager):
    if len(user_manager.get_all_users()) < 3:
        pytest.skip("Not enough users to test")
    assert len(user_manager.get_all_users()) >= 3
