class DynamicProperties:
    """
    Клас для динамічного додавання властивостей до екземпляра під час виконання.
    """

    def add_property(self, prop_name, default_value=None):
        """
        Додає нову властивість до класу під час виконання.

        Arguments:
            prop_name (str): Назва нової властивості.
            default_value: Початкове значення для нової властивості (за замовчуванням None).

        Return:
            None
        """

        storage = {prop_name: default_value}

        def getter(self):
            """Геттер для нової властивості"""
            return storage[prop_name]

        def setter(self, value):
            """Сеттер для нової властивості"""
            storage[prop_name] = value

        # Додаємо нову property до екземпляра класу
        setattr(self.__class__, prop_name, property(getter, setter))

if __name__ == "__main__":
    # Приклад використання
    obj = DynamicProperties()
    obj.add_property('test_dynamic', 'exmp_name')

    print(obj.test_dynamic)
    obj.test_dynamic = "Python"
    print(obj.test_dynamic)
