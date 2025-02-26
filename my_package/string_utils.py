"""
string_utils.py

Модуль для роботи з рядками.

Містить функції:
    to_upper: Перетворює рядок у верхній регістр.
    cut_whitespace: Обрізає пробіли по початку і кінці рядка.
"""


def to_upper(text: str) -> str:
    """
    Перетворює текст у верхній регістр.

    Arguments:
        text (str): Вхідний рядок.

    Return:
        str: Рядок у верхньому регістрі.
    """
    return text.upper()


def cut_whitespace(text: str) -> str:
    """
    Видаляє пробіли на початку та в кінці рядка.

    Arguments:
        text (str): Вхідний рядок.

    Return:
        str: Рядок без пробілів на початку та в кінці.
    """
    return text.strip()
