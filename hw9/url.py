"""#8"""

import re


def extract_urls(text: str) -> list[str]:
    """
    Виділяє всі URL-адреси з переданого тексту.

    Args:
        text (str): Вхідний текст, з якого потрібно витягнути URL-адреси.

    Returns:
        list[str]: Список знайдених URL-адрес.
    """
    pattern = re.compile(r'https?://(?:www\.)?\S+\b')
    return pattern.findall(text)


if __name__ == "__main__":
    TEXT = """
        Перейдіть за посиланням https://example.com або https://www.example.org/page.
        Також можна відвідати http://test.com/test?q=1.
    """
    print(extract_urls(TEXT))
