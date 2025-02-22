class LimitedAttributesMeta(type):
    """Метаклас, що обмежує кількість атрибутів у класі"""
    MAX_ATTRIBUTES = 3  # Максимальна кількість атрибутів

    def __new__(mcs, name, bases, class_dict):
        """
        Створює новий клас і перевіряє кількість атрибутів.

        Arguments:
            name (str): Назва класу.
            bases (tuple): Кортеж батьківських класів.
            class_dict (dict): Словник атрибутів класу.

        Return:
            type: Створений клас.

        Raise:
            TypeError: Якщо кількість атрибутів перевищує MAX_ATTRIBUTES.
        """
        user_attrs = {k: v for k, v in class_dict.items() if not k.startswith('__')}

        if len(user_attrs) > mcs.MAX_ATTRIBUTES:
            raise TypeError(f"Клас {name} не може мати більше {mcs.MAX_ATTRIBUTES} атрибутів.")

        return super().__new__(mcs, name, bases, class_dict)


if __name__ == "__main__":
    # Створення класу без помилки
    class LimitedClass(metaclass=LimitedAttributesMeta):
        attr1 = 1
        attr2 = 2
        attr3 = 3

    print("-"*20)

    # Створення класу з помилкою
    class InvalidClass(metaclass=LimitedAttributesMeta):
        a = 1
        b = 2
        c = 3
        d = 4
