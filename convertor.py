"""#6"""

import os
import json
import csv
import xml.etree.ElementTree as ET


class CSVToJSON:
    """Клас для перетворення CSV у JSON."""

    @staticmethod
    def convert(csv_path: str, json_path: str) -> None:
        """
        Конвертує CSV-файл у JSON.

        Arguments:
            csv_path (str): Шлях до CSV-файлу.
            json_path (str): Шлях до JSON-файлу.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
            FileNotFoundError: Якщо CSV-файл не існує.
        """
        if not isinstance(csv_path, str):
            raise TypeError("'csv_path' must be 'str'")
        if not isinstance(json_path, str):
            raise TypeError("'json_path' must be 'str'")

        try:
            with open(csv_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {csv_path} не знайдено")
        
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class JSONToCSV:
    """Клас для перетворення JSON у CSV."""

    @staticmethod
    def convert(json_path: str, csv_path: str):
        """
        Конвертує JSON-файл у CSV.

        Arguments:
            json_path (str): Шлях до JSON-файлу.
            csv_path (str): Шлях до CSV-файлу.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
            FileNotFoundError: Якщо JSON-файл не існує.
        """
        if not isinstance(json_path, str):
            raise TypeError("'json_path' must be 'str'")
        if not isinstance(csv_path, str):
            raise TypeError("'csv_path' must be 'str'")

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {json_path} не знайдено")
        
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class XMLToJSON:
    """Клас для перетворення XML у JSON."""
    @staticmethod
    def convert(xml_path: str, json_path: str) -> None:
        """
        Конвертує XML-файл у JSON.

        Arguments:
            xml_path (str): Шлях до XML-файлу.
            json_path (str): Шлях до JSON-файлу.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
            FileNotFoundError: Якщо XML-файл не існує.
        """
        if not isinstance(xml_path, str):
            raise TypeError("'xml_path' must be 'str'")
        if not isinstance(json_path, str):
            raise TypeError("'json_path' must be 'str'")
        
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {xml_path} не знайдено")
        
        def xml_to_dict(element):
            result = {}
            for child in element:
                tag = child.tag
                
                if len(child) > 0:
                    value = xml_to_dict(child)
                else:
                    value = child.text

                if tag in result:
                    if isinstance(result[tag], list):
                        result[tag].append(value)
                    else:
                        result[tag] = [result[tag], value]
                else:
                    result[tag] = value

            return result

        data = {root.tag: xml_to_dict(root)}

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # Файли вказані із врахуванням, що до цього було запущено `book_store.py` і `students_csv.py`
    CSVToJSON.convert("students.csv", "students.json") 
    JSONToCSV.convert("books.json", "books.csv")
    XMLToJSON.convert('products.xml', 'products.json')
