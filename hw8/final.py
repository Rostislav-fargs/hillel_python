"""#9"""

from typing import Dict, Any


class BaseRepository:
    """Базовий клас репозиторію для збереження даних."""

    def save(self, data: Dict[str, Any]) -> None:
        """
        Метод для збереження даних.

        Arguments:
            data (Dict[str, Any]): Дані для збереження.

        Raises:
            NotImplementedError: Якщо метод не перевизначено в дочірньому класі.
        """
        raise NotImplementedError("Метод 'save' має бути перевизначений у підкласі")


class SQLRepository(BaseRepository):
    """Конкретний клас для роботи з SQL-базами даних."""

    def save(self, data: Dict[str, Any]) -> None:
        """Зберігає дані у SQL-базі (імітація)."""
        print(f"збереження до SQL: {data}")


if __name__ == "__main__":
    repo = SQLRepository()
    repo.save({"name": "Product1", "price": 10.5})  # Викликаємо метод save

    # Викличе помилку, бо метод save не перевизначений
    # base_repo = BaseRepository()
    # base_repo.save({"name": "Test"})  # NotImplementedError
