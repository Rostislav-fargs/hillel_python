"""#6"""

import re


def is_strong_password(password: str) -> bool:
    """
    Перевірка валідності пароля.

    Пароль має містити принаймні одну малу літеру, одну велику літеру,
    одну цифру, один спеціальний символ (@, #, $, %, &) і бути довжиною від 8 символів.

    Arguments:
        password (str): Пароль для перевірки.

    Returns:
        bool: True, якщо пароль коректний, і False, якщо ні.
    """
    pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&])[A-Za-z\d@#$%&]{8,}$'
    )
    return bool(pattern.match(password))


if __name__ == "__main__":
    PASSWORDS = [
        "SomePassw",
        "SomePassw1",
        "SomePassw@2",
        "Some#Passw3",
        "somepassw",
        "p@assw0rD"
    ]
    for pwd in PASSWORDS:
        print(f"{pwd}: {is_strong_password(pwd)}")
