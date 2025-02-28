"""6.2"""

import pytest
from unittest.mock import MagicMock

from bank_account import BankAccount


# Фікстура для створення екземпляра BankAccount з початковим балансом
@pytest.fixture
def bank_account():
    return BankAccount(initial_balance=100.0)


# Тест поповнення рахунку
def test_deposit(bank_account):
    bank_account.deposit(50.0)
    assert bank_account.get_balance() == 150.0


# Тест зняття грошей з рахунку
def test_withdraw(bank_account):
    bank_account.withdraw(30.0)
    assert bank_account.get_balance() == 70.0


# Тест зняття суми більше ніж доступно на рахунку
def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(ValueError, match="Недостатньо коштів на рахунку"):
        bank_account.withdraw(200.0)


# Тест поповнення нулем і від'ємним значенням
@pytest.mark.parametrize("amount", [-10, 0])
def test_invalid_deposit(amount, bank_account):
    with pytest.raises(ValueError, match="Сума поповнення має бути більше 0"):
        bank_account.deposit(amount)


# Тест зняття нуля і від'ємного значення
@pytest.mark.parametrize("amount", [-5, 0])
def test_invalid_withdraw(amount, bank_account):
    with pytest.raises(ValueError, match="Сума зняття має бути більше 0"):
        bank_account.withdraw(amount)


# Тестування отримання балансу з рахунку
def test_mock_external_balance_check():
    bank_account = BankAccount(100)
    external_api = MagicMock()
    external_api.get_balance.return_value = bank_account.get_balance()
    
    assert external_api.get_balance() == 100
    external_api.get_balance.assert_called_once()


# Skip тесту, коли баланс дорівнює нулю
@pytest.mark.skipif(BankAccount(0).get_balance() == 0, reason="Рахунок порожній, тест пропущено")
def test_skip_withdraw_empty_account():
    account = BankAccount(0)
    with pytest.raises(ValueError, match="Недостатньо коштів на рахунку"):
        account.withdraw(100)
