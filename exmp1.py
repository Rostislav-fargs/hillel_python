import pprint


def analyze_object(obj):
    """
    Виводить дані про наданий об'єкт.

    Arguments:
        obj : Будь-який об'єкт.

    Return:
        None
    """
    obj_info = {
        "type": type(obj).__name__, 
        "methods_and_attributes": [],  
    }

    for attribute_name in dir(obj):
        try:
            attribute_value = getattr(obj, attribute_name)
            attribute_type = type(attribute_value).__name__
            obj_info["methods_and_attributes"].append({
                "name": attribute_name,
                "type": attribute_type,
            })
        except Exception as e:
            obj_info["methods_and_attributes"].append({
                "name": attribute_name,
                "type": type(e).__name__,
                "error": str(e),
            })

    pprint.pprint(obj_info, width=80)


# Тестові об'єкти
test_objects = [
    3.14,  # Число з плаваючою комою (float)
    "Hello, World!",  # Рядок (str)
    True,  # Логічне значення (bool)
    None,  # NoneType
    [1, 2, 3],  # Список (list)
    {"key": "value"},  # Словник (dict)
    bytes("test", encoding="utf-8"),  # Байтовий рядок (bytes)
]


class ExampleClass:
    """Просто тестовий клас"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


if __name__ == "__main__":
    test_objects.append( ExampleClass)

    # Тестовий виклик функції через цикл за списком об'єктів
    for exmp_obj in test_objects:
        print("-"*80)
        analyze_object(exmp_obj)
