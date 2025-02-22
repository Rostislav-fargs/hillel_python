class Proxy:
    """
    Клас Proxy, який дозволяє перехоплювати виклики методів і атрибутів об'єкта.
    """

    def __init__(self, obj):
        """
        Ініціалізує Proxy об'єкт, який буде обгорнутий.

        Arguments:
            obj: Об'єкт, для якого створюється проксі.
        """
        self._obj = obj

    def __getattr__(self, name):
        """
        Перехоплює виклики атрибутів і методів об'єкта і додає додаткову поведінку.

        Arguments:
            name (str): Назва атрибута чи методу, до якого здійснюється доступ.

        Return:
            Можливий атрибут або метод об'єкта, або wrapper функція, якщо атрибут є методом.
        """
        attr = getattr(self._obj, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                print(f"Calling method: {name} with args: {args} and kwargs: {kwargs}")
                return attr(*args, **kwargs)
            return wrapper
        return attr

class MyClass:
    """
    Приклад класу, що має метод `greet` для вітання.
    """
    def greet(self, name):
        return f"Hello, {name}!"

if __name__ == "__main__":
    obj = MyClass()
    proxy = Proxy(obj)

    print(proxy.greet("Alice"))
