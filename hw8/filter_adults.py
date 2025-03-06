"""#2"""

from typing import List, Tuple


def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Фільтрує список людей, залишаючи тільки тих, хто досяг повноліття.

    Arguments::
        people (List[Tuple[str, int]]): Список людей, кожен елемент якого є кортежем
            з імені (str) і віку (int).

    Returns:
        List[Tuple[str, int]]: Список людей, що досягли повноліття (вік >= 18).
    
    Raises:
        TypeError: Якщо 'people' не є списком або елементи не є кортежами з правильними типами.
        ValueError: Якщо вік людини менше нуля.
    """
    if not isinstance(people, list):
        raise TypeError("'people' має бути списком")
    if not people:
        raise TypeError("'people' не може бути порожнім списком")

    for person in people:
        if not isinstance(person, tuple):
            raise TypeError("елементи 'people' мають бути кортежами")
        if not isinstance(person[0], str) or not isinstance(person[1], int):
            raise TypeError(
                "кортежі 'people' повинні вміщати ім'я(str) на першій позиції і вік(int) на другій"
            )
        if person[1] < 0:
            raise ValueError("вік не може бути менше нуля")

    return [person for person in people if person[1] >= 18]


if __name__ == "__main__":
    people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
    print(filter_adults(people)) # [("Андрій", 25), ("Марія", 19)]
