class SingletonMeta(type):
    """Метаклас, що реалізує патерн Singleton"""
    _instances = {}

    def __call__(mcs, *args, **kwargs):
        """
        Створює або повертає єдиний екземпляр класу.

        Arguments:
            *args: Аргументи для ініціалізації класу.
            **kwargs: Ключові аргументи для ініціалізації класу.

        Return:
            object: Єдиний екземпляр класу.
        """
        if mcs not in mcs._instances:
            mcs._instances[mcs] = super().__call__(*args, **kwargs)
        return mcs._instances[mcs]


# Клас, що використовує SingletonMeta
class Singleton(metaclass=SingletonMeta):
    """
    Клас, що використовує метаклас SingletonMeta.
    """
    def __init__(self):
        print("Creating instance")

if __name__ == "__main__":
    # Приклад використання
    obj1 = Singleton()  # Creating instance
    obj2 = Singleton()  # Не створює новий екземпляр

    print(obj1 is obj2)  # True
