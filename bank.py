from abc import ABC, abstractmethod

from transaction import Transaction
from users import Admin, General


class Bank:
    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
        self.__balance = 10000
        self.__total_loan = 5000
        self.__is_loan_available = True
        self.admins = []
        self.accounts = []

    def create_admin_account(self, user_name, email, bank_instance):
        account = Admin(user_name, email, bank_instance)
        self.admins.append(account)
        return account

    def create_General_account(self, user_name, email):
        account = General(user_name, email)
        self.accounts.append(account)
        return account

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, transaction):
        self.__balance += transaction.amount

    @property
    def is_loan_available(self):
        return self.__is_loan_available

    @is_loan_available.setter
    def is_loan_available(self, status):
        self.__is_loan_available = bool(status)

    @property
    def total_loan(self):
        return self.__total_loan

    def status(self):
        if self.__balance == 0:
            return f'The {self.bank_name} bank is bankrupt 🤣'
        else:
            return f'The {self.bank_name} bank is running 😀'
