"""#2"""

import uuid


class UniqueIDIterator:
    """Ітератор, який генерує унікальні ідентифікатори UUID."""

    def __init__(self) -> None:
        self.current_id = uuid.uuid4()


    def __iter__(self) -> "UniqueIDIterator":
        """Повертає ітератор."""
        return self


    def __next__(self) -> str:
        """
        Генерує і повертає UUID.

        Return:
            str: Новий UUID.
        """
        unique_id = uuid.uuid4()
        return unique_id


if __name__ == "__main__":
    uid_iter = UniqueIDIterator()
    for _ in range(5):
        print(next(uid_iter))
