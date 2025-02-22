def analyze_inheritance(cls):
    """
    Аналізує наслідування класу і виводить методи, які були успадковані.

    Arguments:
        cls (type): Клас, для якого здійснюється аналіз наслідування.

    Return:
        None
    """

    print(f"Клас {cls.__name__} наслідує:")

    for base in cls.__bases__:
        inherited_methods = []

        for name, method in base.__dict__.items():
            # Перевірка, чи є це методом (не спеціальний метод, не змінна)
            if callable(method) and not name.startswith('__'):
                if name not in cls.__dict__:
                    inherited_methods.append(name)

        if inherited_methods:
            for method in inherited_methods:
                print(f"- {method} з {base.__name__}")


class Parent:
    """
    Батьківський клас, що містить метод parent_method.
    """

    def parent_method(self):
        pass


class Child(Parent):
    """
    Дочірній клас, що додає власний метод child_method.
    """

    def child_method(self):
        pass


if __name__ == "__main__":
    # Приклад використання
    analyze_inheritance(Child)
