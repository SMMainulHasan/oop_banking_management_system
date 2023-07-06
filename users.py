
from transaction import Transaction


class User:
    def __init__(self, user_name, email) -> None:
        self.name = user_name
        self.email = email


class General(User):
    def __init__(self, user_name, email) -> None:
        self.balance = 0
        self.due_loan = 0
        super().__init__(user_name, email)

    def deposit(self, amount):
        trx = Transaction(amount)
        trx.receiver = self.email
        trx.transaction_type = "deposit"
        self.balance += trx.amount

    def get_loan(self):
        if self.balance > 0:
            applicable_amount = self.balance / 2
            loan_trans = Transaction(applicable_amount)
            return f"Request successful, you got {applicable_amount} as loan"
        else:
            return "You don't have the author to set the bank's loan status"


class Admin(User):
    def __init__(self, user_name, email, bank) -> None:
        self.bank = bank
        super().__init__(user_name, email)

    def total_balance(self):
        return self.bank.balance

    def total_loan(self):
        return self.bank.total_loan

    def active_loan_status(self):
        self.bank.is_loan_available = True

    def inactive_loan_stats(self):
        self.bank.is_loan_available = False
