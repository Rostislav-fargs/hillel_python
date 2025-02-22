import inspect


def analyze_module(module_name: str) -> None:
    """
    Аналізує наданий модуль.

    Arguments:
        module_name (str): Назва модулю для аналізу.

    Return:
        None
    """

    try:
        module = __import__(module_name)
    except ImportError:
        print(f"Модуль '{module_name}' не знайдено.")
        return

    functions = inspect.getmembers(
        module,
        lambda obj: inspect.isfunction(obj) or inspect.isbuiltin(obj)
    )
    classes = inspect.getmembers(module, inspect.isclass)

    print("Функції:")
    if functions:
        for name, func in functions:
            try:
                signature = inspect.signature(func)
                print(f"- {name}{signature}")
            except ValueError:
                # Якщо неможливо отримати підпис (наприклад, для вбудованої функції)
                print(f"- {name} (підпис не доступний)")
    else:
        print("- <немає функцій>")

    print("\nКласи:")
    if classes:
        for name, cls in classes:
            print(f"- {name}")
    else:
        print("- <немає класів>")


# Приклад використання
if __name__ == "__main__":
    print("Аналіз модуля math:")
    analyze_module("math")
