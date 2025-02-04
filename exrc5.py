import pprint


class InsufficientFundsException(Exception):
    """
    Exception raised when a user attempts a transaction with insufficient funds.

    Attributes:
        required_amount (float): The amount of money required for the transaction.
        current_balance (float): The current balance in the user's account.
        currency (str): The currency of the account.
        transaction_type (str): The type of transaction (e.g., "withdraw_cash", "deposit_funds").
    """

    def __init__(self, required_amount, current_balance, currency, transaction_type):
        super().__init__(
            f"Недостатньо коштів для транкзакції '{transaction_type}'."
            f"Баланс: {current_balance} {currency}."
            f"Необіхдно: {required_amount} {currency}."
        )
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type


class BankTransactions:
    """
    A class that represents bank transactions, including deposits and withdrawals.

    Attributes:
        current_balance (float): The current balance in the user's account.
        currency (str): The currency of the account (default is "USD").
    """

    def __init__(self, current_balance=0.0, currency="USD"):
        """
        Initializes the BankTransactions object with a starting balance and currency.

        Args:
            current_balance (float): The starting balance of the account (default is 0.0).
            currency (str): The currency of the account (default is "USD").
        """

        self.current_balance = current_balance
        self.currency = currency

    def _make_transaction(self, amount, transaction_type, deposit_funds=False) -> dict:
        """
        A private method that processes a transaction. It checks whether the user has enough funds
        and either performs the deposit or withdrawal.

        Args:
            amount (float): The amount to be transacted (either deposited or withdrawn).
            transaction_type (str): The type of transaction (e.g., "withdraw_cash", "deposit_funds").
            deposit_funds (bool): A flag to indicate whether the transaction is a deposit (True) or a withdrawal (False).

        Returns:
            dict: A dictionary containing the transaction type, status, current balance, and operation amount.
        """

        try:
            success_transaction = None
            if not deposit_funds and self.current_balance < amount:
                raise InsufficientFundsException(
                    required_amount=amount, 
                    current_balance=self.current_balance, 
                    currency=self.currency, 
                    transaction_type="withdraw_cash"
                )
            else:
                self.current_balance += amount if deposit_funds else -amount
                success_transaction = True

        except InsufficientFundsException as e:
            print(e)

        finally:
            response = {
                "transaction_type" : transaction_type,
                "status" : "success" if success_transaction else "failed",
                "current_balance" : self.current_balance,
                "operation_amount" : amount
            }
            return response

    def withdraw_cash(self, amount) -> dict:
        """
        Initiates a withdrawal transaction.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            dict: A dictionary with the result of the transaction, including status and updated balance.
        """

        return self._make_transaction(amount, "withdraw_cash")

    def deposit_funds(self, amount) -> dict:
        """
        Initiates a deposit transaction.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            dict: A dictionary with the result of the transaction, including status and updated balance.
        """

        return self._make_transaction(amount, "deposit_funds", True)


if __name__ == "__main__":
    # створення об'єкту-рахунку клієнта(за певною валютою)
    bt_uah = BankTransactions(26, "UAH")

    # спроба зняти готівку
    w_c1 = bt_uah.withdraw_cash(70)
    pprint.pprint(w_c1)

    # поповнення балансу
    d_f1 = bt_uah.deposit_funds(100)
    pprint.pprint(d_f1)

    # друга спроба зняти готівку
    w_c2 = bt_uah.withdraw_cash(120)
    pprint.pprint(w_c2)
