def log_methods(cls):
    """
    Декоратор, який логуватиме виклики методів класу, виводячи їх аргументи.

    Arguments:
        cls: Клас, до якого застосовується декоратор.

    Return:
        class: Клас з обгорнутими методами для логування.
    """
    for name, method in list(cls.__dict__.items()):
        if callable(method) and not name.startswith('__'):
            def wrapper(method_name, orig_method):
                """
                Обгортка для методів, що додає логування.

                Arguments:
                    orig_method: Оригінальний метод, до якого додається логування.

                Return:
                    function: Обгортка, яка логуватиме виклики методу.
                """
                def wrapped(self, *args, **kwargs):
                    print(f"Logging: {method_name} called with {args}")
                    return orig_method(self, *args, **kwargs)
                return wrapped

            setattr(cls, name, wrapper(name, method))
    return cls


@log_methods
class MyClass:
    """
    Клас, що містить методи для виконання арифметичних операцій.
    """

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
print(obj.add(5, 3))
print(obj.subtract(5, 3))
