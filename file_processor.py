"""#7.1"""


class FileProcessor:
    """Клас для роботи з файлами."""

    @staticmethod
    def write_to_file(file_path: str, data: str):
        """
        Записує дані у файл.

        Arguments:
            file_path (str): Шлях до файлу, в який будуть записані дані.
            data (str): Дані, які потрібно записати у файл.

        Returns:
            None
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)


    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Читає дані з файлу.

        Arguments:
            file_path (str): Шлях до файлу, з якого будуть зчитані дані.

        Returns:
            str: Дані, зчитані з файлу.

        Raises:
            FileNotFoundError: Якщо файл не знайдено.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не знайдено")
