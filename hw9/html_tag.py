"""#5"""

import re


def remove_html_tags(text: str) -> str:
    """
    Повертає текст без HTML-тегів.

    Arguments:
        text (str): Вхідний текст із HTML-тегами.

    Returns:
        str: Текст без HTML-тегів.
    """
    pattern = re.compile(r'<.*?>')
    return re.sub(pattern, '', text)


if __name__ == "__main__":
    TEXT = """
        <p>Це <b>жирний</b> текст і <a href='#'>посилання</a>.</p>
        <div>Ще один <span style='color:red;'>червоний</span> текст.</div>
    """
    print(remove_html_tags(TEXT))
