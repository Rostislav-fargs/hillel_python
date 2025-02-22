class TypeCheckedMeta(type):
    """
    Метаклас, який додає перевірку типів для атрибутів класу, використовуючи анотації.
    """

    def __new__(mcs, name, bases, dct):
        new_cls = super().__new__(mcs, name, bases, dct)

        def __setattr__(self, name, value):
            if name in self.__annotations__:
                expected_type = self.__annotations__[name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Для атрибута '{name}' очікується тип '{expected_type.__name__}', "
                        f"але отримано '{type(value).__name__}'."
                    )
            super(new_cls, self).__setattr__(name, value)

        setattr(new_cls, '__setattr__', __setattr__)

        return new_cls


class Person(metaclass=TypeCheckedMeta):
    """Клас для демонстрації автоматичної перевірки типів атрибутів."""
    name: str = ""
    age: int = 0


# Приклад використання
if __name__ == "__main__":
    p = Person()
    p.name = "John"
    print(p.name)

    # Помилка через неправильний тип
    try:
        p.age = "30"
    except TypeError as e:
        print(e)
