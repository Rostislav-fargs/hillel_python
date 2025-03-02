"""#3"""

import re


def extract_hashtags(text: str) -> list[str]:
    """
    Виділяє всі хештеги з переданого тексту.

    Argumets:
        text (str): Вхідний текст, з якого потрібно витягнути хештеги.

    Returns:
        list[str]: Список знайдених хештегів.
    """
    pattern = re.compile(r'#\w+')
    return pattern.findall(text)


if __name__ == "__main__":
    TEXT = """
        Сьогодні чудовий день! #sunny #weather123 #hello-world
        Але #Sunday все одно найкраща! #100DaysOfCode
    """
    print(extract_hashtags(TEXT))
