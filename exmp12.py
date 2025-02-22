class LoggingMeta(type):
    """
    Метаклас для логування доступу та зміни атрибутів класу.

    Логування виконується кожного разу, коли відбувається доступ або зміна атрибута.
    """

    def __new__(mcs, name, bases, dct):
        """
        Створює клас і перевизначає методи для логування доступу та змін атрибутів.
        """
        original_getattribute = dct.get('__getattribute__')
        original_setattr = dct.get('__setattr__')

        def __getattribute__(self, key):
            print(f"Logging: accessed '{key}'")  # Логування перед доступом до атрибуту
            if original_getattribute:
                return original_getattribute(self, key)
            return super(type(self), self).__getattribute__(key)

        def __setattr__(self, key, value):
            print(f"Logging: modified '{key}'")  # Логування перед зміною атрибуту
            if original_setattr:
                return original_setattr(self, key, value)
            super(type(self), self).__setattr__(key, value)

        dct['__getattribute__'] = __getattribute__
        dct['__setattr__'] = __setattr__

        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=LoggingMeta):
    """Клас для демонстрації логування геттера і сеттера."""
    def __init__(self, name):
        self.name = name


# Приклад використання
if __name__ == "__main__":
    obj = MyClass("Python")
    print(obj.name)
    obj.name = "New Python"
    print(obj.name)
