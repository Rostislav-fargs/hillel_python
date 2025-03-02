"""#4"""

import re


def format_date(date_str: str) -> str | None:
    """
    Перетворює дату з формату DD/MM/YYYY у формат YYYY-MM-DD.

    Arguments:
        date_str (str): Рядок із датою у форматі DD/MM/YYYY.

    Returns:
        str: Дата у форматі YYYY-MM-DD або повідомлення про помилку.
        None: Якщо вхідний формат дати неправильний.
    """
    pattern = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    match = pattern.match(date_str)
    if match:
        day, month, year = match.groups()
        return f"{year}-{month}-{day}"
    return None


if __name__ == "__main__":
    dates = [
        "25/12/2023",
        "01/01/2024",
        "31/07/1999",
        "12-05-2022",
    ]
    for date in dates:
        print(f"{date} -> {format_date(date)}")
