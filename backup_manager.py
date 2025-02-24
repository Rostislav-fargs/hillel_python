"""#9"""

import os
import shutil


class BackupManager:
    """
    Менеджер резервного копіювання файлів.

    Автоматично створює резервну копію перед внесенням змін у файл та 
    відновлює її у разі помилки.

    Attributes:
        file_path (str): Шлях до основного файлу.
        backup_path (str): Шлях до резервної копії.
    """

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.backup_path = f"{file_path}.backup"


    def __enter__(self) -> "BackupManager":
        """
        Створює резервну копію файлу при вході у контекст.

        Returns:
            BackupManager: Об'єкт менеджера резервного копіювання.
        """
        if os.path.exists(self.file_path):
            shutil.copy2(self.file_path, self.backup_path)
        return self


    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Видаляє резервну копію, якщо немає помилки, або відновлює файл у разі збою.
        """
        if exc_type is None:
            if os.path.exists(self.backup_path):
                os.remove(self.backup_path)
        else:
            if os.path.exists(self.backup_path):
                shutil.move(self.backup_path, self.file_path)


if __name__ == "__main__":
    TEST_FILE = "test_file.txt"

    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write("Original content")

    try:
        with BackupManager(TEST_FILE):
            with open(TEST_FILE, "w", encoding="utf-8") as f:
                f.write("New content")
            # Навмисне викликана помилка для відновлення вмісту
            raise RuntimeError("Імітація помилки")
    except RuntimeError:
        pass
