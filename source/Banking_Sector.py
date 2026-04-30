import re

class TransferError(Exception):
    pass

def transfer(from_account, to_account, amount, balance):
    account_number_pattern = r"^\d{10}"

    if not re.match(account_number_pattern, from_account):
        raise TransferError("Invalid account number")

    elif amount <= 0:
        raise TransferError("Amount must be positive")

    elif amount > balance:
        raise TransferError("Amount exceeds balance")

    else:
        return True

