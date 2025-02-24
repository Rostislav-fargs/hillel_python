"""#7"""

import re
from typing import Generator


def error_log_generator(log_file: str) -> Generator[str, None, None]:
    """
    Генератор для зчитування лог-файлу та фільтрації рядків з помилками (4XX або 5XX).

    Arguments:
        log_file (str): Шлях до файлу.
    
    Return:
        str: Рядок, в якому містився код помилки 4xx або 5xx
    """
    # патерн для фільтрування рядків
    error_pattern = re.compile(r'\b(4\d{2}|5\d{2})\b')

    with open(log_file, 'r', encoding="uft-8") as file:
        for line in file:
            if error_pattern.search(line):
                yield line


if __name__ == "__main__":
    INPUT_FILE_PATH = "logs.txt"
    OUTPUT_FILE_PATH = "errors.txt"

    error_generator = error_log_generator(INPUT_FILE_PATH)

    with open(OUTPUT_FILE_PATH, 'w', encoding="utf-8") as output_file:
        for error_line in error_generator:
            output_file.write(error_line)
