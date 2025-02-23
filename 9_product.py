class ProductWithGetSet:
    """
    Клас, що представляє продукт з методами get/set для ціни.
    
    Attributes:
        name (str): Назва продукту.
        _price (float): Ціна продукту.
    """

    def __init__(self, name: str, price: float):
        """
        Ініціалізує об'єкт продукту, перевіряючи коректність даних.

        Arguments:
            name (str): Назва продукту.
            price (float): Початкова ціна продукту.
        """
        self.name = name.strip()
        self.set_price(price)

    def get_price(self) -> float | None:
        """
        Повертає ціну продукту.
        
        Returns:
            float | None: Ціна продукту.
        """
        return self.__dict__.get('price', None)

    def set_price(self, value: float):
        """
        Встановлює ціну продукту після перевірки.
        
        Arguments:
            value (float): Нова ціна продукту.
        
        Raises:
            ValueError: Якщо ціна є від'ємною.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__dict__["price"] = value


class ProductWithProperty:
    """
    Клас, що представляє продукт із властивістю (property) для ціни.
    
    Attributes:
        name (str): Назва продукту.
        _price (float): Ціна продукту.
    """

    def __init__(self, name: str, price: float):
        """
        Ініціалізує об'єкт продукту, перевіряючи коректність даних.
        
        Arguments:
            name (str): Назва продукту.
            price (float): Початкова ціна продукту.
        """
        self.name = name.strip()
        self.price = price

    @property
    def price(self) -> float | None:
        """
        Повертає ціну продукту.
        
        Returns:
            float | None: Ціна продукту.
        """
        return self.__dict__.get('price', None)

    @price.setter
    def price(self, value: float):
        """
        Встановлює ціну продукту після перевірки.
        
        Arguments:
            value (float): Нова ціна продукту.
        
        Raises:
            ValueError: Якщо ціна є від'ємною.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__dict__['price'] = value


class PriceDescriptor:
    """
    Дескриптор для керування ціною продукту у вибраній валюті.
    """

    exchange_rates = {
        "UAH": 1.0,
        "USD": 41.64,
        "EUR": 43.57,
    }

    def __get__(self, instance, owner) -> float:
        """
        Повертає ціну у вибраній валюті.
        """
        if instance is None:
            return self
        base_price = instance.__dict__.get("_price_uah", 0)
        currency = instance.__dict__.get("_currency", "UAH")
        return round(base_price / self.exchange_rates[currency], 2)

    def __set__(self, instance, value: float):
        """
        Встановлює ціну у гривнях після перевірки.

        Raises:
            ValueError: Якщо ціна є від'ємною або має неправильний тип.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be 'int' or 'float'")
        if value < 0:
            raise ValueError("Price cannot be negative")

        currency = instance.__dict__.get("_currency", "UAH")
        instance.__dict__["_price_uah"] = round(value * self.exchange_rates[currency], 2)


class CurrencyDescriptor:
    """
    Дескриптор для керування валютою.
    """

    allowed_currencies = {"UAH", "USD", "EUR"}

    def __get__(self, instance, owner) -> str:
        """Повертає поточну валюту."""
        if instance is None:
            return self
        return instance.__dict__.get("_currency", "UAH")

    def __set__(self, instance, value: str):
        """Встановлює нову валюту, змінюючи ціну відповідно до курсу."""
        if value not in self.allowed_currencies:
            raise ValueError(f"Currency must be one of {self.allowed_currencies}")

        old_currency = instance.__dict__.get("_currency", "UAH")
        if old_currency != value:
            # Конвертуємо ціну з поточної валюти у гривні
            price_in_uah = instance.__dict__.get("_price_uah", 0)
            instance.__dict__["_currency"] = value
            # Оновлюємо ціну у гривнях відповідно до нової валюти
            instance.__dict__["_price_uah"] = price_in_uah


class ProductWithDescriptor:
    """
    Клас, що представляє продукт із дескриптором для ціни та валюти.
    """

    price = PriceDescriptor()
    currency = CurrencyDescriptor()

    def __init__(self, name: str, price: float, currency: str = "UAH"):
        """
        Ініціалізує об'єкт продукту, перевіряючи коректність даних.

        Arguments:
            name (str): Назва продукту.
            price (float): Початкова ціна продукту.
            currency (str): Валюта ("UAH", "USD" або "EUR").
        """
        self.name = name.strip()
        self.currency = currency
        self.price = price


def test_product_classes():
    for ProductClass in [ProductWithGetSet, ProductWithProperty, ProductWithDescriptor]:
        print(f"Testing {ProductClass.__name__}")
        try:
            # Створення продукту
            if ProductClass is ProductWithDescriptor:
                product = ProductClass("Laptop", 1000, "UAH")
            else:
                product = ProductClass("Laptop", 1000)

            # Отримання початкової ціни
            price = product.get_price() if hasattr(product, "get_price") else product.price
            print("Initial price:", price)

            # Зміна ціни
            try:
                if hasattr(product, "set_price"):
                    product.set_price(1500)
                else:
                    product.price = 1500
                price = product.get_price() if hasattr(product, "get_price") else product.price
                print("Updated price:", price)
            except ValueError as e:
                print("Caught error when updating price:", e)

            # Встановлення від'ємної ціни
            try:
                if hasattr(product, "set_price"):
                    product.set_price(-500)
                else:
                    product.price = -500
            except ValueError as e:
                print("Caught error when setting negative price:", e)

            # Додатковий тест для ProductWithDescriptor: зміна валюти
            if ProductClass is ProductWithDescriptor:
                print("Currency before:", product.currency)
                product.currency = "USD"
                print("Currency after:", product.currency)
                print("Price in new currency:", product.price)

        except Exception as e:
            print("Error in test:", e)
        print()


if __name__ == "__main__":
    test_product_classes()

    # Testing ProductWithGetSet
    # Initial price: 1000
    # Updated price: 1500
    # Caught error when setting negative price: Price cannot be negative

    # Testing ProductWithProperty
    # Initial price: 1000
    # Updated price: 1500
    # Caught error when setting negative price: Price cannot be negative

    # Testing ProductWithDescriptor
    # Initial price: 1000.0
    # Updated price: 1500.0
    # Caught error when setting negative price: Price cannot be negative
    # Currency before: UAH
    # Currency after: USD
    # Price in new currency: 36.02
