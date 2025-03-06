"""#1"""


def calculate_discount(price: float, discount: float) -> float:
    """
    Обчислює ціну зі знижкою.

    Arguments:
        price (float): Початкова ціна.
        discount (float): Знижка у відсотках.

    Returns:
        float: Ціна зі знижкою.

    Raises:
        TypeError: Якщо `price` або `discount` не є числами типу float.
        ValueError: Якщо `price` <= 0 або `discount` < 0.
    """
    if not isinstance(price, float):
        raise TypeError("'price' має бути 'float'")
    if not isinstance(discount, float):
        raise TypeError("'discount' має бути 'float'")
    if price <= 0:
        raise ValueError("'price' має бути більше нуля")
    if 0 > discount:
        raise ValueError("'discount' має дорівнювати або бути вище за нуль")

    if discount > 100:
        return 0.0

    return price * (1 - discount / 100)


if __name__ == "__main__":
    print(calculate_discount(100.0, 20.0))   # 80.0
    print(calculate_discount(50.0, 110.0))   # 0.0
