class BinaryNumber:
    """Клас для представлення двійкового числа та виконання бітових операцій."""

    def __init__(self, value: str):
        """
        Ініціалізація об'єкта BinaryNumber.

        Arguments:
            value (str): Двійкове число у вигляді рядка.
        
        Raises:
            ValueError: Якщо значення не є допустимим двійковим числом.
        """
        if not all(bit in '01' for bit in value):
            raise ValueError("Value must be a binary string.")
        self.value = value

    def __and__(self, other):
        """
        Виконує операцію AND для двійкових чисел.

        Arguments:
            other (BinaryNumber): Інший об'єкт класу BinaryNumber.

        Returns:
            BinaryNumber: Результат операції AND.
        """
        max_len = max(len(self.value), len(other.value))
        self_padded = self.value.zfill(max_len)
        other_padded = other.value.zfill(max_len)
        result = ''.join('1' if self_padded[i] == '1' and other_padded[i] == '1' else '0'
                         for i in range(max_len))
        return BinaryNumber(result)

    def __or__(self, other):
        """
        Виконує операцію OR для двійкових чисел.

        Arguments:
            other (BinaryNumber): Інший об'єкт класу BinaryNumber.

        Returns:
            BinaryNumber: Результат операції OR.
        """
        max_len = max(len(self.value), len(other.value))
        self_padded = self.value.zfill(max_len)
        other_padded = other.value.zfill(max_len)
        result = ''.join('1' if self_padded[i] == '1' or other_padded[i] == '1' else '0'
                         for i in range(max_len))
        return BinaryNumber(result)

    def __xor__(self, other):
        """
        Виконує операцію XOR для двійкових чисел.

        Arguments:
            other (BinaryNumber): Інший об'єкт класу BinaryNumber.

        Returns:
            BinaryNumber: Результат операції XOR.
        """
        max_len = max(len(self.value), len(other.value))
        self_padded = self.value.zfill(max_len)
        other_padded = other.value.zfill(max_len)
        result = ''.join('1' if self_padded[i] != other_padded[i] else '0'
                         for i in range(max_len))
        return BinaryNumber(result)

    def __invert__(self):
        """
        Виконує операцію NOT для двійкового числа.

        Returns:
            BinaryNumber: Результат операції NOT.
        """
        result = ''.join('1' if bit == '0' else '0' for bit in self.value)
        return BinaryNumber(result)

    def __repr__(self):
        """
        Повертає строкове подання двійкового числа.

        Returns:
            str: Строка, що представляє двійкове число.
        """
        return f"BinaryNumber({self.value})"


# Тестування бітових операцій
if __name__ == "__main__":
    # Створення двійкових чисел
    num1 = BinaryNumber("1101")  # 13 в десятковій системі
    num2 = BinaryNumber("1011")  # 11 в десятковій системі

    # Операція AND
    result_and = num1 & num2
    # BinaryNumber(1101) & BinaryNumber(1011) = BinaryNumber(1001)
    print(f"{num1} & {num2} = {result_and}")

    # Операція OR
    result_or = num1 | num2
    # BinaryNumber(1101) | BinaryNumber(1011) = BinaryNumber(1111)
    print(f"{num1} | {num2} = {result_or}")

    # Операція XOR
    result_xor = num1 ^ num2
    # BinaryNumber(1101) ^ BinaryNumber(1011) = BinaryNumber(0110)
    print(f"{num1} ^ {num2} = {result_xor}")

    # Операція NOT
    result_not = num1
    # BinaryNumber(1101) = BinaryNumber(1101)
    print(f"{num1} = {result_not}")
