"""
    OOP:   i) Class/Object -> Encapsulation
          ii) Inheritance  -> Re-usability
         iii) Polymorphism -> Agility -> Inheritance -> Class
"""
from typing import Type


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


# account          -> base class, super class
# checking_account -> sub class, derived class
class checking_account(account):
    def __init__(self, iban, balance=0, overdraft_amount=500):
        super().__init__(iban, balance)
        self.overdraft_amount = overdraft_amount

    def withdraw(self, amount):  # overriding
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive.")
        if amount > (self.balance + self.overdraft_amount):  # business rule
            raise InsufficientBalanceException(reason="Your balance does not cover your expenses."
                                               , deficit=amount - self.balance - self.overdraft_amount)
        self.balance -= amount

    def __str__(self):  # overriding
        return f"checking_account (iban={self.iban}, balance={self.balance}, overdraft_amount={self.overdraft_amount})"


class customer:
    """
    attributes: full_name: str, tc_kimlik_no: str, accounts: {}
    methods: __init__ ✔
             __str__ ✔
             add_account ✔
             remove_account ✔
             get_account ✔
             get_total_balance ✔
             fun
    deadline: 11:10
    """

    def __init__(self, full_name, tc_kimlik_no, *accounts):
        self.full_name = full_name
        self.tc_kimlik_no = tc_kimlik_no
        self.accounts = dict()
        for acc in accounts:
            self.accounts[acc.iban] = acc

    def fun(self, amount=10):
        for acc in self.accounts.values():
            acc.withdraw(amount)

    def add_account(self, acc):
        self.accounts[acc.iban] = acc

    def get_account(self, iban):
        return self.accounts[iban]

    def remove_account(self, iban):
        del self.accounts[iban]

    def get_total_balance(self, mode="functional"):
        if mode == "functional":
            return sum(map(lambda acc: acc.balance, self.accounts.values()))
        total = 0
        for acc in self.accounts.values():
            total += acc.balance
        return total

    def summarize_dict_methods(self):
        for iban, acc in self.accounts.items():
            print(f"{iban}: {acc}")

        for iban in self.accounts.keys():
            print(f"{iban}: {self.accounts[iban]}")

        for acc in self.accounts.values():
            print(f"{acc.iban}: {acc}")

    def __str__(self):
        return f"customer (full_name: {self.full_name}, kimlik: {self.tc_kimlik_no}," \
               f" number of accounts: {len(self.accounts)}, " \
               f" total balance: {self.get_total_balance()})"


try:
    jack = customer("jack bauer", "11111111110",
                    account("tr1", 10_000),
                    checking_account("tr2", 5_000, 1_250),
                    account("tr3", 50_000))
    jack.add_account(checking_account("tr4", 500_000, 10_000))
    jack.remove_account("tr2")
    print(jack)
    jack.summarize_dict_methods()

    acc1 = account(iban="tr1", balance=10_000)
    acc2 = checking_account(iban="tr2", balance=20_000, overdraft_amount=1_000)
    print(acc1)
    print(float(acc1))
    acc1.withdraw(2_500)
    print(f"balance is {acc1.balance}")
    acc1.deposit(5_000)
    print(f"balance is {acc1.balance}")
    acc1.withdraw(12_500)
    print(f"balance is {acc1.balance}")
    acc2.withdraw(21_000)
    print(acc2)
    print(isinstance(acc1, account))  # True
    print(isinstance(acc1, checking_account))  # False
    print(isinstance(acc2, checking_account))  # True
    print(isinstance(acc2, account))  # True ? False -> True
    # acc2 -> class checking_account(account) -> class account(object) -> object
    print(isinstance(acc1, object))  # True ? False -> True
    print(isinstance(acc2, object))  # True ? False -> True
    print(isinstance(42, object))  # True ? False -> True : 42 -> int -> object
    print(isinstance(42, int))  # True ? False
    print(isinstance(True, bool))  # True ? False
    print(isinstance(3.1415, float))  # True ? False
    print(isinstance("jack shephard", str))  # True ? False
except ValueError as err:
    print(err)
except InsufficientBalanceException as err:
    print(f"Reason: {err.reason}")
    print(f"Deficit: {err.deficit}")
