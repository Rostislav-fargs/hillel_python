"""#10"""

import zipfile
import os


class ZipArchiveManager:
    """Менеджер для роботи з архівом zip."""

    def __init__(self, archive_name: str) -> None:
        """
        Ініціалізує менеджер архіву.

        Arguments:
            archive_name (str): Назва архіву.
        """
        self.archive_name: str = archive_name
        self.zip_file = None


    def __enter__(self) -> "ZipArchiveManager":
        """
        Відкриває архів для запису.

        Returns:
            ZipArchiveManager: Повертає екземпляр класу.
        """
        self.zip_file = zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED)
        return self


    def add_file(self, file_path, arcname=None) -> None:
        """
        Додає файл в архів.

        Arguments:
            file_path (str): Шлях до файлу, який додається.
            arcname (str): Ім'я файлу в архіві.
                Якщо не вказано, то використовується справжнє ім'я.
        """
        if self.zip_file:
            self.zip_file.write(file_path, arcname if arcname else os.path.basename(file_path))


    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Закриває архів після завершення роботи."""
        if self.zip_file:
            self.zip_file.close()


if __name__ == "__main__":
    with ZipArchiveManager("archive.zip") as archive:
        REQUIREMENTS = "requirements.txt"
        NUMBERS = "numbers.txt"
        archive.add_file(REQUIREMENTS)
        archive.add_file(NUMBERS)
