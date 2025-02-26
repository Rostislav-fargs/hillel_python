"""#5"""

import os
import xml.etree.ElementTree as ET


class ProductInventory:
    """Клас для роботи з кількість товарів в XML фалі."""

    def __init__(self, file_path: str) -> None:
        """
        Ініціалізує об'єкт для роботи з інвентарем продуктів.

        Arguments:
            file_path (str): Шлях до XML файлу з даними продуктів.

        Raises:
            TypeError: Якщо file_path не є рядком.
            FileNotFoundError: Якщо файл не існує за вказаним шляхом.
        """
        if not isinstance(file_path, str):
            raise TypeError("'file_path' must be 'str'")
        if not os.path.exists(file_path):
            raise FileNotFoundError()

        self.file_path: str = file_path
        self.tree = None
        self.root = None


    def __enter__(self) -> "ProductInventory":
        """
        Відкриває XML файл при вході у контекст.

        Return:
            ProductInventory: Об'єкт класу для роботи з даними продуктів.
        """
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()
        return self


    def get_products(self):
        """
        Отримує список продуктів з XML файлу.

        Return:
            list: Список словників, де кожен словник містить інформацію про продукт (назва, ціна, кількість).
        """
        return [
            {
                "product": str(product.find("name").text),
                "price": float(product.find("price").text),
                "quantity": int(product.find("quantity").text),
            } for product in self.root.findall("product")
        ]


    def update_quantity(self, product_name: str, quantity: int):
        """
        Оновлює кількість продукту в XML файлі.

        Arguments:
            product_name (str): Назва продукту, кількість якого потрібно оновити.
            quantity (int): Нова кількість продукту.

        Raises:
            TypeError: Якщо product_name не є рядком або quantity не є цілим числом.
            ValueError: Якщо продукт не знайдено в інвентарі.
        """
        if not isinstance(product_name, str):
            raise TypeError("'product_name' must be 'str'")
        if not isinstance(quantity, int):
            raise TypeError("'quantity' must be 'int'")

        for product in self.root.findall("product"):
            if product.find("name").text == product_name:
                product.find("quantity").text = str(quantity)
                break
        else:
            raise ValueError(f"Продукт '{product_name}' не знайдено.")
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Зберігає зміни в XML файлі при виході з контексту."""
        if exc_type is None:
            self.tree.write(self.file_path, encoding="UTF-8", xml_declaration=True)


if __name__ == "__main__":
    XML_FILE = "products.xml"

    with ProductInventory(XML_FILE) as inventory:
        data = inventory.get_products()[0]

        inventory.update_quantity(data['product'], 88)