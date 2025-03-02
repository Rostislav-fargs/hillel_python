"""#1"""

import re


def is_valid_email(email: str) -> bool:
    """
    Перевіряє чи є рядок коректною електронною поштою.

    Arguments:
        email (str): Рядок, який потрібно перевірити.

    Returns:
        bool: True, якщо email відповідає шаблону, інакше False.
    """
    pattern = re.compile(
        r'^[a-zA-Z0-9](\.?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
    )
    return bool(pattern.match(email))


if __name__ == "__main__":
    emails = [
        "valid.email@example.com",
        "invalid..email@example.com",
        "invalidemail@.com",
        "invalidemail@com",
        "valid123@domain.org",
        "user.name@sub.domain.net",
    ]

    for example in emails:
        print(f"{example}: {is_valid_email(example)}")
