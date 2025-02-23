from decimal import Decimal, ROUND_HALF_UP


class Price:
    """Клас для представлення ціни товару з округленням до двох десяткових знаків."""

    def __init__(self, amount):
        """
        Ініціалізація об'єкта Price.

        Arguments:
            amount (float | str | Decimal): Значення ціни.

        Raises:
            ValueError: Якщо значення ціни від'ємне.
        """
        self.amount = self._round_price(amount)

    @staticmethod
    def _round_price(value):
        """
        Округлює значення ціни до двох знаків після коми.

        Arguments:
            value (float | str | Decimal): Значення для округлення.

        Returns:
            Decimal: Округлене значення.
        """
        price = Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        return price

    def __add__(self, other):
        """
        Додавання двох цін.

        Arguments:
            other (Price): Інший об'єкт класу Price.

        Returns:
            Price: Новий об'єкт Price з доданою вартістю.
        """
        return Price(self.amount + other.amount)

    def __sub__(self, other):
        """
        Віднімання двох цін.

        Arguments:
            other (Price): Інший об'єкт класу Price.

        Returns:
            Price: Новий об'єкт Price з віднятою вартістю.

        Raises:
            ValueError: Якщо результат від'ємний.
        """
        new_amount = self.amount - other.amount
        if new_amount < 0:
            raise ValueError("Результат віднімання не може бути від'ємним")
        return Price(new_amount)

    def __lt__(self, other):
        """Менше за іншу ціну."""
        return self.amount < other.amount

    def __eq__(self, other):
        """Перевірка на рівність двох цін."""
        return self.amount == other.amount

    def __repr__(self):
        """Повертає строкове представлення ціни."""
        return f"Price({self.amount})"

    @classmethod
    def from_string(cls, price_str):
        """
        Створює об'єкт Price з рядкового представлення.

        Arguments:
            price_str (str): Рядок, що містить число.

        Returns:
            Price: Новий об'єкт Price.
        """
        return cls(Decimal(price_str))


if __name__ == "__main__":
    price1 = Price(10.456)
    price2 = Price("5.99")

    print(f"Ціна 1: {price1}, Ціна 2: {price2}")
    print(f"Сума: {price1 + price2}")
    print(f"Різниця: {price1 - price2}")
    print(f"price1 < price2: {price1 < price2}")
    print(f"price1 == Price(10.46): {price1 == Price(10.46)}")
    print(f"З рядка: {Price.from_string('12.349')}")

    # Ціна 1: Price(10.46), Ціна 2: Price(5.99)
    # Сума: Price(16.45)
    # Різниця: Price(4.47)
    # price1 < price2: False
    # price1 == Price(10.46): True
    # З рядка: Price(12.35)
