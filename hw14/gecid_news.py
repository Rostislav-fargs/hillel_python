"""
Отримання новин з Gecid.com
Парсинг, запис до csv та аналіз.
"""

from typing import Optional, List, Dict, Tuple
from datetime import datetime, timedelta
import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd


GECID_NEWS_URL = "https://ua.gecid.com/news/"


def get_page(url: str, idt: int=None) -> Optional[BeautifulSoup]:
    """
    Отримує HTML-сторінку за вказаним URL, з можливістю додавання додаткового параметра idt.

    Arguments:
        url (str): URL сторінки для отримання.
        idt (Optional[int]): Додатковий параметр для побудови URL (за замовчуванням None).

    Returns:
        Optional[BeautifulSoup]: Об'єкт BeautifulSoup або None у разі помилки.

    Raises:
        TypeError: Якщо `idt` не є int.
    """
    if idt and not isinstance(idt, int):
        raise TypeError("'idt' повинен бути int")

    try:
        # Якщо надано idt, то робиться запит за іншим url
        if idt:
            url = f"https://ua.gecid.com/getNextNewsFeed.php?b=8&idt=0&db={idt}"

        response = requests.get(url=url, timeout=10)
        response.raise_for_status()

        return BeautifulSoup(response.text, 'html5lib')

    except requests.exceptions.MissingSchema:
        print("Невірний формат URL.")
    except requests.exceptions.ConnectionError:
        print("Неможливо встановити з'єднання.")
    except requests.exceptions.Timeout:
        print("Час очікування відповіді вичерпано.")
    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}")

    return None


def parse_news(soup: BeautifulSoup, days_limit: int) -> Tuple[Optional[int], List[Dict[str, str]]]:
    """
    Отримує HTML-сторінку та повертає список новин у вигляді словників.

    Arguments:
        soup (BeautifulSoup): Об'єкт BeautifulSoup, що містить HTML-сторінку.
        days_limit (int): Кількість днів для фільтрації новин.

    Returns:
        Tuple[Optional[int], List[Dict[str, str]]]: Кортеж, що містить 
            ID наступної сторінки та список новин (словники).

    Raises:
        TypeError: Якщо `soup` не є об'єктом BeautifulSoup або `days_limit` не є int.
        ValueError: Якщо `days_limit` менше 0.
    """
    if not isinstance(soup, BeautifulSoup):
        raise TypeError("'soup' повинен бути BeautifulSoup")
    if not isinstance(days_limit, int):
        raise TypeError("'days_limit' повинен бути int")
    if days_limit < 0:
        raise ValueError("'days_limit' повинен дорівнювати або бути більше 0")

    news_list = []

    # Знаходимо наступний id для пагінації
    next_id_tag = soup.find('input', {'name': 'date[]'})
    next_id = int(next_id_tag['value']) if next_id_tag else 0

    # Знаходимо всі блоки новин
    news_blocks = soup.find_all("div", class_="news")

    # Дата для фільтрації
    today = datetime.today()
    cutoff_date = today - timedelta(days=days_limit)

    for block in news_blocks:
        # Дата публікації новини
        date_tag = block.find("time")
        date = (
            date_tag["datetime"]
            if date_tag and date_tag.has_attr("datetime")
            else "Без дати"
        )

        # Перетворення дати в datetime для порівняння
        try:
            news_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            news_date = None

        # Якщо новина старіше за days_limit, то новина не обробляється
        if news_date and news_date < cutoff_date:
            continue

        # Заголовок новини
        title_tag = block.find("h2") or block.find("h1")
        title = title_tag.text.strip() if title_tag else "Без заголовка"

        # Посилання на новину
        link_tag = block.find("a", class_="fixed_news")
        link = str(
            GECID_NEWS_URL + link_tag["href"].strip("./news")
            if link_tag and link_tag.has_attr("href")
            else "Без посилання"
        )

        # Короткий опис новини
        summary_tag = block.find("p")
        summary = summary_tag.text.strip() if summary_tag else "Без опису"

        news_list.append({
            "title": title,
            "link": link,
            "date": date,
            "summary": summary
        })

    return next_id, news_list


def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    """
    Зберігає список новин у CSV-файл.

    Arguments:
        data (List[Dict[str, str]]): Список новин, кожна з яких представлена словником.
        filename (str): Назва файлу для збереження. За замовчуванням "news.csv".

    Raises:
        TypeError: Якщо `data` не є списком словників або `filename` не є str.
        OSError: Якщо сталася помилка під час запису у файл.
    """
    if not isinstance(data, list) or not all(isinstance(news, dict) for news in data):
        raise TypeError("'data' повинен бути списком словників.")
    if not isinstance(filename, str):
        raise TypeError("'filename' повинен бути str")

    if not data:
        print("Попередження: отримано порожній список. Запис у файл не виконано.")
        return None

    fieldnames = ["title", "link", "date", "summary"]

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Запис заголовків, якщо файл порожній
            if file.tell() == 0:
                writer.writeheader()

            writer.writerows(data)  # Записуємо список одразу, без циклу

        print(f"Збережено {len(data)} записів у {filename}")

    except OSError as e:
        print(f"Помилка запису у файл '{filename}': {e}")

    return None


def analyze_data(filename: str="news.csv") -> None:
    """
    Зчитує дані з CSV та виводить статистику публікацій по днях.

    Arguments:
        filename (str): Шлях до CSV-файлу з новинами. За замовчуванням 'news.csv'.

    Raises:
        TypeError: Якщо `filename` не str.
        FileNotFoundError: Якщо файл не знайдено.
        pd.errors.EmptyDataError: Якщо файл порожній.
        KeyError: Якщо в файлі відсутній стовпець 'date'.
    """
    if not isinstance(filename, str):
        raise TypeError("'filename' повинен бути str")
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Помилка: файл '{filename}' порожній.")
        return None

    if "date" not in df.columns:
        print("Помилка: у CSV-файлі немає стовпця 'date'.")
        return None

    # Перетворюємо дату в тип datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    if df["date"].isna().all():
        print("Помилка: неможливо розпізнати жодної дати у стовпці 'date'.")
        return None

    # Групуємо новини за датою
    news_count_by_day = df.groupby(df['date'].dt.date).size()

    # Виводимо статистику
    print("Статистика публікацій за днями:")
    print(news_count_by_day)

    return None



def run_main(pages: int=10, days_limit: int=7) -> None:
    """
    Запускає процес отримання, обробки та збереження новин.

    Arguments:
        pages (int): Кількість сторінок для обробки.
        days_limit (int): Обмеження по даті (новини старші за цей ліміт ігноруються).

    Raises:
        TypeError: Якщо `pages` або `days_limit` не є цілими числами.
        ValueError: Якщо `pages < 1` або `days_limit < 0`.
    """
    if not isinstance(pages, int) or not isinstance(days_limit, int):
        raise TypeError("'pages' і 'days_limit' повинні бути int.")
    if pages < 1:
        raise ValueError("'pages' повинно бути >= 1.")
    if days_limit < 0:
        raise ValueError("'days_limit' повинно бути >= 0.")

    current_page = None

    for page in range(pages):
        soup = get_page(GECID_NEWS_URL, current_page)

        if not soup:
            print(f"Помилка: сторінку {page} не вдалося завантажити.")
            break

        current_page, news_data = parse_news(soup, days_limit=days_limit)

        if news_data:
            save_to_csv(news_data, "gecid_news.csv")
        else:
            print(f"Сторінка {page}: новин немає або всі новини старші за {days_limit} днів.")

    analyze_data("gecid_news.csv")


if __name__ == "__main__":
    run_main()
