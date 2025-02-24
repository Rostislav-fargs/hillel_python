"""#4"""


def filter_lines(input_file: str, keyword: str) -> str:
    """
    Генератор, що читає великий файл рядок за рядком 
        і повертає лише ті, що містять keyword.
    
    Arguments:
        input_file (str): Шлях до вхідного файлу.
        keyword (str): Ключове слово для фільтрації рядків.
    
    Yields:
        str: Рядок, який містить ключове слово.
    """
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            if keyword in line:
                yield line.strip()


def save_filtered_lines(input_file: str, output_file: str, keyword: str) -> None:
    """
    Фільтрує рядки у файлі та записує їх у новий файл.
    
    Arguments:
        input_file (str): Шлях до вхідного файлу.
        output_file (str): Шлях до вивідного файлу.
        keyword (str): Ключове слово для фільтрації рядків.
    """
    with open(output_file, "w", encoding="utf-8") as out_file:
        for line in filter_lines(input_file, keyword):
            out_file.write(line + "\n")


if __name__ == "__main__":
    INPUT_FILE = "logs.txt"
    OUTPUT_FILE = "errors.txt"
    KEYWORD = "ERROR"

    save_filtered_lines(INPUT_FILE, OUTPUT_FILE, KEYWORD)
