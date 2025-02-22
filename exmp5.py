class MutableClass:
    """
    Клас для динамічного додавання та видалення атрибутів у об'єкта.
    """

    def add_attribute(self, name: str, value: str):
        """
        Додає атрибут з ім'ям `name` та значенням `value` до об'єкта.

        Arguments:
            name (str): Назва атрибута.
            value (str): Значення атрибута.

        Return:
            None
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str):
        """
        Видаляє атрибут з ім'ям `name`, якщо він існує.

        Arguments:
            name (str): Назва атрибута для видалення.

        Raise:
            AttributeError: Якщо атрибут з такою назвою не існує.

        Return:
            None
        """
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"Атрибут '{name}' не знайдено")


if __name__ == "__main__":
    # Приклад використання
    obj = MutableClass()
    obj.add_attribute("color", "blue")
    print(obj.color)  # Виведе: blue

    obj.remove_attribute("color")
    print(hasattr(obj, "color"))  # Виведе: False
