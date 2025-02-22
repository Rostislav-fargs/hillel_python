import random
import datetime


def create_class(class_name: str, methods: dict):
    """
    Повертає створений за наданою назвою і методами клас.

    Arguments:
        class_name (str): Назва класу.
        methods (dict): Словник, що містить методи класу.

    Return:
        class: Динамічно створений клас.
    """
    return type(class_name, (object,), methods)


def random_day(self):
    """Повертає випадковий день тижня."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return random.choice(days)


def random_time(self):
    """Повертає випадковий час доби"""
    return datetime.datetime.now().strftime("%H:%M:%S")


# Приклад використання
if __name__ == "__main__":
    methods = {
        "random_day": random_day,
        "random_time": random_time
    }

    MyDynamicClass = create_class("MyDynamicClass", methods)
    obj = MyDynamicClass()
    print("Тестування динамічного класу:")
    print("Випадковий день:", obj.random_day())
    print("Випадковий час:", obj.random_time())
