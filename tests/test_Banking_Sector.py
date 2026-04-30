import pytest

import source.Banking_Sector as Bank

def test_transfer():
    account_from = "1282312931"
    account_to = "232032421"
    amount = 100
    balance = 1000

    result = Bank.transfer(account_from, account_to, amount, balance)
    assert result == True


def test_insufficient_balance():
    account_from = "1282312931"
    account_to = "232032421"
    amount = 100
    balance = 0

    with pytest.raises(Bank.TransferError, match="Amount exceeds balance"):
        Bank.transfer(account_from, account_to, amount, balance)

def test_account_number():
    account_from = "12823129"
    account_to = "232032421"
    amount = 100
    balance = 1000

    with pytest.raises(Bank.TransferError, match = "Invalid account number"):
        Bank.transfer(account_from, account_to, amount, balance)

def test_amount():
    account_from = "1282312931"
    account_to = "232032421"
    amount = 0
    balance = 1000

    with pytest.raises(Bank.TransferError, match = "Amount must be positive"):
        Bank.transfer(account_from, account_to, amount, balance)