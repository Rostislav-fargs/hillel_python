"""#3"""

import os
import csv
from PIL import Image


class ImageMetadataIterator:
    """
    Ітератор для збору метаданих зображень у каталозі та запису їх у CSV.

    Attributes:
        directory (str): Шлях до каталогу зображень.
        output_csv (str): Шлях до файлу CSV.
        image_paths (list[str]): Список шляхів до зображень.
    """

    img_formats: tuple[str] = ("jpg", "jpeg", "png", "bmp", "gif", "tiff")

    def __init__(self, directory: str, output_csv: str="image_metadata.csv") -> None:
        """
        Ініціалізує ітератор, зчитує список зображень та створює файл CSV.

        Arguments:
            directory (str): Шлях до каталогу.
            output_csv (str): Ім'я файлу для запису метаданих 
                (за замовчуванням "image_metadata.csv").
        
        Raises:
            FileNotFoundError: Якщо каталог не існує.
            ValueError: Якщо в каталозі немає зображень.
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Каталог '{directory}' не знайдено.")
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' не є каталогом.")

        self.directory: str = directory
        self.image_paths: list[str] = [
            os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(self.img_formats)
        ]
        self.output_csv: str = output_csv
        self.index: int = 0

        with open(self.output_csv, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["File Name", "Format", "Size (px)", "Mode"])


    def __iter__(self) -> "ImageMetadataIterator":
        "Повертає ітератор."
        return self


    def __next__(self) -> dict[str, str] | None:
        """
        Повертає метадані наступного зображення у каталозі.
        Дописує дані до csv файлу (output_csv).

        Returns:
            dict[str, str] | None: Словник з інформацією про зображення або None у разі помилки.

        Raises:
            StopIteration: Якщо файли закінчились.
        """
        if self.index >= len(self.image_paths):
            raise StopIteration

        image_path = self.image_paths[self.index]
        self.index += 1

        try:
            with Image.open(image_path) as img:
                metadata = {
                    "File Name": os.path.basename(image_path),
                    "Format": img.format,
                    "Size (px)": f"{img.size[0]}x{img.size[1]}",
                    "Mode": img.mode,
                }

                with open(self.output_csv, mode="a", encoding="utf-8", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(metadata.values())

                return metadata

        except Exception as e:
            print(f"Помилка при обробці {image_path}: {e}")
            return None


if __name__ == "__main__":
    IMG_DIR = "images"
    iterator = ImageMetadataIterator(IMG_DIR)

    for image_info in iterator:
        print(image_info)
