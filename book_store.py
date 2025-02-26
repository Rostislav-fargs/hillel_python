"""#4"""

import json
from datetime import datetime


class Book:
    """Клас для опису книги."""

    def __init__(self, book: str, author: str, year: int, available: bool) -> None:
        """
        Ініціалізує книгу.

        Arguments:
            book (str): Назва книги.
            author (str): Автор книги.
            year (int): Рік видання.
            available (bool): Чи є книга в наявності.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
            ValueError: Якщо рік перевищує поточний рік.
        """
        if not isinstance(book, str):
            raise TypeError(f"'book' must be 'str' not {type(book).__name__}")
        if not isinstance(author, str):
            raise TypeError(f"'author' must be 'str' not {type(author).__name__}")
        if not isinstance(year, int):
            raise TypeError(f"'year' must be 'int' not {type(year).__name__}")
        if not isinstance(available, bool):
            raise TypeError(f"'available' must be 'bool' not {type(available).__name__}")
        if not year < datetime.now().year:
            raise ValueError("the 'year' cannot be higher than the current one")

        self.book: str = book
        self.author: str = author
        self.year: int = year
        self.available: bool = available


    def to_dict(self):
        """
        Повертає дані про об'єкт в форматі словника.
        
        Return:
            dit: Дані про книжку.
        """
        return {
            "назва": self.book,
            "автор": self.author,
            "рік": self.year,
            "наявність": self.available
        }


    def __str__(self):
        return (f"{self.book}, автор: {self.author}, рік: {self.year}, "
            f"{'є в наявності' if self.available else 'відсутня'}"
            )


class BookStore:
    """Книгарня."""

    def __init__(self, file_path: str) -> None:
        """
        Ініціалізує книгарню.

        Arguments:
            file_path (str): Шлях до файлу для збереження книг.

        Raises:
            TypeError: Якщо шлях до файлу не є рядком.
        """
        if not isinstance(file_path, str):
            raise TypeError()
        self.file_path: str = file_path
        self.books: list = self.load_books()


    def load_books(self):
        """
        Завантажує книги з JSON-файлу.

        Return:
            list: Список об'єктів класу Book.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                books = json.load(file)
                return [Book(*book.values()) for book in books]
        except FileNotFoundError:
            return []


    def save_books(self):
        """Зберігає книги у JSON файл."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)


    def add_book(self, book: "Book"):
        """
        Додає нову книгу у бібліотеку.

        Arguments:
            book (Book): Об'єкт книги.

        Raises:
            TypeError: Якщо аргумент не є об'єктом класу Book.
        """
        if not isinstance(book, Book):
            raise TypeError("'book' must be 'Book'")

        self.books.append(book)
        self.save_books()


    def get_available_books(self):
        """
        Повертає список доступних книг.

        Return:
            list: Список доступних книг.
        """
        return [book for book in self.books if book.available]


    def display_available_books(self):
        """Виводить список доступних книг."""
        available_books = self.get_available_books()
        if available_books:
            print("Доступні книги:")
            for book in available_books:
                print(book)
        else:
            print("Немає доступних книг.")


if __name__ == "__main__":
    store = BookStore("books.json")
    books_to_add = [
        Book("Дюна", "Френк Герберт", 2008, True),
        Book("1984", "Джордж Орвелл", 2018, False),
        Book("Кобзар", "Тарас Шевченко", 2004, True)
    ]
    for book_obj in books_to_add:
        store.add_book(book_obj)

    store.display_available_books()
