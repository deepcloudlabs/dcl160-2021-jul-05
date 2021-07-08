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
        print("account -> withdraw")
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


# account          -> base class, super class
# checking_account -> sub class, derived class
class checking_account(account):
    def __init__(self, iban, balance=0, overdraft_amount=500):
        super().__init__(iban, balance)
        self.overdraft_amount = overdraft_amount

    def withdraw(self, amount):  # overriding
        print("checking_account -> withdraw")
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive.")
        if amount > (self.balance + self.overdraft_amount):  # business rule
            raise InsufficientBalanceException(reason="Your balance does not cover your expenses."
                                               , deficit=amount - self.balance - self.overdraft_amount)
        self.balance -= amount

    def __str__(self):  # overriding
        return f"checking_account (iban={self.iban}, balance={self.balance}, overdraft_amount={self.overdraft_amount})"


from random import randint

acc = None  # account, checking_account, savings_account, ...
# polymorphic behaviour -> deposit, withdraw

r = randint(1, 6)
if r <= 3:
    acc = account("tr1", 100_000)
else:
    acc = checking_account("tr2", 200_000, 5_000)

print(acc)
acc.withdraw(10_000)  # account-> widthdraw ? checking_account -> withdraw
