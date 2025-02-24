"""#6"""

import os


class DirectoryFileIterator:
    """
    Ітератор для перебору файлів у вказаному каталозі.

    Attributes:
        directory (str): Шлях до каталогу.
        files (list[str]): Список файлів у каталозі.
    """

    def __init__(self, directory: str) -> None:
        """
        Ініціалізує ітератор для файлів у каталозі.

        Arguments:
            directory (str): Шлях до каталогу.
        
        Raises:
            FileNotFoundError: Якщо вказаний каталог не існує.
            NotADirectoryError: Якщо передано не каталог.
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        self.directory: str = directory
        self.files: list[str] = [
            f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        self.index: int = 0


    def __iter__(self) -> "DirectoryFileIterator":
        """Повертає ітератор."""
        return self


    def __next__(self) -> tuple[str, int]:
        """
        Повертає наступний файл у каталозі разом із його розміром.

        Returns:
            Tuple[str, int]: Ім'я файлу та його розмір у байтах.

        Raises:
            StopIteration: Якщо файли закінчились.
        """
        if self.index >= len(self.files):
            raise StopIteration

        file_name = self.files[self.index]
        file_path = os.path.join(self.directory, file_name)
        file_size = os.path.getsize(file_path)

        self.index += 1

        return file_name, file_size


if __name__ == "__main__":
    DIRECTORY = "."
    file_iterator = DirectoryFileIterator(DIRECTORY)

    print(f"File{'':<31}Size")
    for name, size in file_iterator:
        print(f"{name:<35}{size} bytes")
