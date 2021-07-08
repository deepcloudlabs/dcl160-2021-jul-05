class InsufficientBalanceException(Exception):
    def __init__(self, reason, deficit):
        self.reason = reason
        self.deficit = deficit


class account(object):
    # constructor
    def __init__(self, iban, balance=0):
        """
        Creates an account with attributes: iban and balance
        :param iban: identifies the account uniquely
        :param balance: stores amount of fiat money
        """
        self.iban = iban  # new attribute -> initialized
        self.balance = balance  # new attribute -> initialized

    def deposit(self, amount):
        """
        Customer add fiat money to account
        :param amount: amount of fiat money
        :return: None
        """
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Customer subtracts fiat money from account
        :param amount: amount of fiat money
        :return: None
        :raise InsufficientBalanceException if amount > balance
        :raise ValueError if amount <= 0
        """
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive.")
        if amount > self.balance:  # business rule
            raise InsufficientBalanceException(reason="Your balance does not cover your expenses."
                                               , deficit=amount - self.balance)
        self.balance -= amount

    def __str__(self):
        return f"account (iban={self.iban}, balance={self.balance})"

    def __float__(self):
        return float(self.balance)


try:
    acc1 = account(iban="tr1", balance=10_000)
    print(acc1)
    print(float(acc1))
    acc1.withdraw(2_500)
    print(f"balance is {acc1.balance}")
    acc1.deposit(5_000)
    print(f"balance is {acc1.balance}")
    acc1.withdraw(12_500)
    print(f"balance is {acc1.balance}")
    acc1.withdraw(-1)
except ValueError as err:
    print(err)
except InsufficientBalanceException as err:
    print(f"Reason: {err.reason}")
    print(f"Deficit: {err.deficit}")
