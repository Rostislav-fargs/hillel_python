"""6.1"""


class BankAccount:
    """Клас для представлення банківського рахунку."""
    def __init__(self, initial_balance: float = 0.0) -> None:
        """
        Ініціалізує банківський рахунок з початковим балансом.

        Arguments:
            initial_balance (float): Початковий баланс рахунку.
                За замовчуванням 0.0.
        """
        self.balance = initial_balance


    def deposit(self, amount: float) -> None:
        """
        Поповнює рахунок на вказану суму.

        Arguments:
            amount (float): Сума поповнення.

        Raises:
            ValueError: Якщо сума поповнення менша або дорівнює 0.
        """
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більше 0")
        self.balance += amount


    def withdraw(self, amount: float) -> None:
        """
        Знімає з рахунку вказану суму, якщо на рахунку достатньо коштів.

        Arguments:
            amount (float): Сума зняття.

        Raises:
            ValueError: Якщо сума зняття менша або дорівнює 0, або якщо на рахунку недостатньо коштів.
        """
        if amount <= 0:
            raise ValueError("Сума зняття має бути більше 0")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.balance -= amount


    def get_balance(self) -> float:
        """
        Повертає поточний баланс рахунку.

        Returns:
            float: Поточний баланс рахунку.
        """
        return self.balance
