"""#4"""

from typing import TypeVar, List, Optional


T = TypeVar("T")


def get_first(lst: List[T]) -> Optional[T]:
    """
    Повертає перший елемент списку або None, якщо список порожній.

    Arguments:
        lst (List[T]): Вхідний список.

    Returns:
        Optional[T]: Перший елемент списку або None.
    """
    return lst[0] if lst else None


if __name__ == "__main__":
    print(get_first([1, 2, 3]))       # 1
    print(get_first(["a", "b", "c"])) # "a"
    print(get_first([]))              # None
