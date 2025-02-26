"""#3"""

import csv
import os
from typing import Generator

class StudentData:
    """Клас для роботи з даними студентів у CSV файлі."""

    def __init__(self, file_path: str) -> None:
        """
        Ініціалізує об'єкт StudentData.

        Arguments:
            file_path (str): Шлях до файлу з даними студентів.

        Raises:
            TypeError: Якщо file_path не є рядком.
        """
        if not isinstance(file_path, str):
            raise TypeError("'file_path' must be 'str'")
        self.file_path: str=file_path


    def create_file(self) -> None:
        """Створює новий CSV файл з заголовками для даних студентів."""
        with open(self.file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Ім'я", "Вік", "Оцінка"])


    def add_student(self, name: str, age: int, point: int) -> None:
        """
        Додає дані нового студента до CSV файлу.

        Arguments:
            name (str): Ім'я студента.
            age (int): Вік студента.
            point (int): Оцінка студента.

        Raises:
            TypeError: Якщо name, age або point мають невірний тип.
        """
        if not isinstance(name, str):
            raise TypeError("'name' must be 'str'")
        if not isinstance(age, int):
            raise TypeError("'age' must be 'int'")
        if not isinstance(point, int):
            raise TypeError("'point' must be 'int'")

        if not os.path.exists(self.file_path):
            self.create_file()

        with open(self.file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, point])


    def get_students(self) -> Generator[dict, None, None] | None:
        """
        Отримує всіх студентів з файлу.

        Return:
            generator: Генератор студентів у вигляді словників, де ключі — це заголовки CSV файлу.
            None: Якщо файл не існує.
        """
        if not os.path.exists(self.file_path):
            return None
        with open(self.file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            yield from reader


    def get_average_point(self) -> float | None:
        """
        Обчислює середню оцінку студентів.

        Return:
            float: Середня оцінка студентів.
            None: Якщо не вдалося обчислити (наприклад, студенти відсутні).
        """
        students = self.get_students()
        if not students:
            return None

        count = 0
        total = 0

        for student in self.get_students():
            try:
                count += 1
                total += float(student["Оцінка"])
            except TypeError:
                continue

        if count == 0:
            return None

        return total / count


if __name__ == "__main__":
    student_file = StudentData("students.csv")
    student_file.add_student('Петро', 21, 90)
    student_file.add_student('Марина', 22, 85)
    student_file.add_student('Андрій', 20, 88)
    print(student_file.get_average_point())
