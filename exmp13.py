class AutoMethodMeta(type):
    """
    Метаклас для автоматичного створення геттерів і сеттерів для атрибутів класу.

    Створює методи `get_<attribute>` та `set_<attribute>` для кожного атрибута класу,
    за винятком тих, які починаються з '__'.
    """

    def __new__(mcs, name, bases, dct):
        """
        Створює клас і додає до нього методи для автоматичного доступу до атрибутів.

        Arguments:
            name (str): Назва класу.
            bases (tuple): Батьківські класи.
            dct (dict): Атрибути класу.

        Return:
            type: Створений клас з автоматично доданими методами.
        """
        methods = {}

        for attr, value in dct.items():
            if not attr.startswith('__'):
                def getter(self, attr=attr):
                    return getattr(self, attr)

                def setter(self, value, attr=attr):
                    setattr(self, attr, value)

                methods[f'get_{attr}'] = getter
                methods[f'set_{attr}'] = setter

        dct.update(methods)

        return super().__new__(mcs, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    """Клас для демонстрації автоматичного додавання геттерів і сеттерів."""
    name = "John"
    age = 30


# Приклад використання
if __name__ == "__main__":
    p = Person()
    print(p.get_name())
    p.set_age(31)
    print(p.get_age())
