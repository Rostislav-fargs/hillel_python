"""#7"""

from typing import TypedDict, Protocol, Optional

# Опис класу User за допомогою TypedDict
class User(TypedDict):
    id: int
    name: str
    is_admin: bool

# Опис протоколу UserDatabase
class UserDatabase(Protocol):
    def get_user(self, user_id: int) -> Optional[User]:
        pass
    
    def save_user(self, user: User) -> None:
        pass

# Реалізація класу InMemoryUserDB
class InMemoryUserDB:
    def __init__(self):
        self.users = {}

    def get_user(self, user_id: int) -> Optional[User]:
        """Отримує користувача за ID."""
        return self.users.get(user_id)

    def save_user(self, user: User) -> None:
        """Зберігає або оновлює користувача."""
        self.users[user['id']] = user


if __name__ == "__main__":
    db = InMemoryUserDB()

    # Створюємо кілька користувачів
    user1 = User(id=1, name="Alice", is_admin=True)
    user2 = User(id=2, name="Bob", is_admin=False)

    # Зберігаємо користувачів
    db.save_user(user1)
    db.save_user(user2)

    # Отримуємо користувачів
    print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": True}
    print(db.get_user(2))  # {"id": 2, "name": "Bob", "is_admin": False}
    print(db.get_user(3))  # None (користувач не знайдений)
