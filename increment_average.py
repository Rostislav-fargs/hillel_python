"""#11"""

from typing import Generator

def increment_average(file_name: str) -> Generator[float, None, None]:
    """
    Обчислює середнє значення чисел з файлу та повертає його після кожного нового числа.

    Arguments:
        file_name (str): Шлях до файлу з числами.
    
    Yields:
        float: Поточне середнє значення після кожного нового числа.
    """

    total = 0
    count = 0

    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                current = float(line.strip())
                total += current
                count += 1
                print(f"current: {current}, total: {total}, count: {count}")
                yield total / count

            except (ValueError, TypeError):
                continue


if __name__ == "__main__":
    for average in increment_average("numbers.txt"):
        print(average)
