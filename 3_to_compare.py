class Person:
    """Клас для представлення особи з ім'ям та віком."""

    def __init__(self, name: str, age: int):
        """
        Ініціалізація об'єкта Person.

        Arguments:
            name (str): Ім'я особи.
            age (int): Вік особи.
        """
        self.name = name
        self.age = age

    def __lt__(self, other: 'Person') -> bool:
        """
        Порівняння за віком: чи поточна особа молодша за іншу.

        Arguments:
            other (Person): Інший об'єкт класу Person.

        Returns:
            bool: True, якщо вік поточної особи менший за вік іншої особи.
        """
        if not isinstance(other, Person):
            raise TypeError("Операція підтримується лише для об'єктів класу Person")
        return self.age < other.age

    def __eq__(self, other: 'Person') -> bool:
        """
        Порівняння за віком: чи однаковий вік у двох осіб.

        Arguments:
            other (Person): Інший об'єкт класу Person.

        Returns:
            bool: True, якщо вік обох осіб однаковий.
        """
        if not isinstance(other, Person):
            raise TypeError("Операція підтримується лише для об'єктів класу Person")
        return self.age == other.age

    def __gt__(self, other: 'Person') -> bool:
        """
        Порівняння за віком: чи поточна особа старша за іншу.

        Arguments:
            other (Person): Інший об'єкт класу Person.

        Returns:
            bool: True, якщо вік поточної особи більший за вік іншої особи.
        """
        if not isinstance(other, Person):
            raise TypeError("Операція підтримується лише для об'єктів класу Person")
        return self.age > other.age

    def __repr__(self) -> str:
        """
        Повертає строкове подання особи.

        Returns:
            str: Строка у форматі "Person(name, age)".
        """
        return f"Person({self.name}, {self.age})"


if __name__ == "__main__":
    # Створення списку осіб
    people = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35),
        Person("David", 25),
        Person("Eva", 40)
    ]

    # Виведення списку до сортування
    print("Вхідний список:")
    for person in people:
        print(person)

    # Сортування списку осіб за віком
    people.sort()

    # Виведення списку після сортування
    print("\nСортований список:")
    for person in people:
        print(person)
