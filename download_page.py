"""#2"""

import requests


def download_web_page(url_address: str) -> str | None:
    """
    Завантажує веб-сторінку та зберігає її в локальний файл.

    Arguments:
        url_address (str): URL-адреса веб-сторінки для завантаження.

    Return:
        str | None: Назва збереженого файлу або None у разі помилки.

    Raises:
        requests.exceptions.RequestException: Якщо виникла помилка під час запиту.
    """
    try:
        response = requests.get(url=url_address, timeout=10)
        response.raise_for_status()

        file_name = url_address.strip('https://').replace('/', '_') + ".html"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(response.text)

        return file_name

    except requests.exceptions.MissingSchema:
        print("Невірний формат URL.")
    except requests.exceptions.ConnectionError:
        print("Неможливо встановити з'єднання.")
    except requests.exceptions.Timeout:
        print("Час очікування відповіді вичерпано.")
    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}")

    return None


if __name__ == "__main__":
    download_web_page("https://monkeytype.com/")
