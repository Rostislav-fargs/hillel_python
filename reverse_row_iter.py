"""#1"""

class ReverseFileIterator:
    """Ітератор рядків зворотньо прочитаного файлу."""

    def __init__(self, file_name: str) -> None:
        """
        Ініціалізує ітератор для зворотного читання файлу.

        Arguments:
            file_name (str): Шлях до файлу для зворотного читання.
        """
        self.file_name: str = file_name
        self.file = None
        self.lines: list[str] = []
        self.cur_line: int = -1

    def __read_file__(self) -> None:
        """Читає файл, розвертає рядки та готує їх до ітерації."""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.lines = file.readlines()
        self.lines.reverse()

    def __iter__(self) -> "ReverseFileIterator":
        """Повертає ітератор, що порядково читає файл."""
        self.__read_file__()
        return self

    def __next__(self) -> str:
        """
        Повертає наступний рядок з файлу.

        Returns:
            str: Наступний рядок файлу, обрізаний від пробілів і нових рядків.
        
        Raises:
            StopIteration: Якщо досягнуто кінця файлу.
        """
        self.cur_line += 1
        if self.cur_line < len(self.lines):
            return self.lines[self.cur_line].strip(' \n')
        raise StopIteration


if __name__ == "__main__":
    NUMBERS = "numbers.txt"
    file_iterator = ReverseFileIterator(NUMBERS)
    for row in file_iterator:
        print(row)
