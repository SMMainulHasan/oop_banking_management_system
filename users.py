from transaction import Transaction


class User:
    def __init__(self, user_name, email, bank) -> None:
        self.name = user_name
        self.email = email
        self.bank = bank


class Admin(User):
    def __init__(self, user_name, email, bank) -> None:
        super().__init__(user_name, email, bank)

    def total_balance(self):
        return self.bank.balance

    def total_loan(self):
        return self.bank.total_loan

    def active_loan_status(self):
        self.bank.is_loan_available = True

    def inactive_loan_stats(self):
        self.bank.is_loan_available = False


class General(User):
    def __init__(self, user_name, email, bank) -> None:
        self.balance = 0
        self.due_loan = 0
        self.transactions = []
        super().__init__(user_name, email, bank)

    def deposit(self, amount):
        trx = Transaction(amount)
        trx.receiver = self.name
        trx.type = "deposit"
        self.balance += trx.amount
        self.bank.balance = trx
        self.transactions.append(trx)

    def withdrawal(self, amount):
        if self.balance >= amount:
            if self.bank.balance >= amount:
                trx = Transaction(amount)
                trx.receiver = self.name
                trx.type = "withdrawal"
                self.balance -= trx.amount
                self.bank.balance = trx
                self.transactions.append(trx)
            else:
                print(
                    f"{self.bank.bank_name} is bankrupt 🤣")
        else:
            print(
                f"{self.name} you don't have the enough money in your account to withdrawal")

    def transfer(self, amount, receiver):
        if self.balance >= amount:
            trx = Transaction(amount)
            trx.sender = self.name
            trx.receiver = receiver.name
            trx.type = "transfer"
            self.balance -= trx.amount
            receiver.balance += trx.amount
            receiver.transactions.append(trx)
            self.transactions.append(trx)
        else:
            print(
                f"{self.name} you don't have the enough money in your account to transfer")

    def get_loan(self):
        if self.balance > 0:
            if self.bank.is_loan_available == True:
                applicable_amount = self.balance * 2
                if self.bank.balance >= applicable_amount:
                    trx = Transaction(applicable_amount)
                    trx.receiver = self.name
                    trx.type = "loan"
                    self.balance += trx.amount
                    self.bank.balance = trx
                    self.transactions.append(trx)
                    print(
                        f"Request successful, {self.name} you got {applicable_amount} as loan")
                else:
                    print("Sorry Currently we don't have the enough liquidity")
            else:
                print("Sorry Currently we don't provide any loan services")
        else:
            print(f"{self.name} you don't have the enough deposit to get loan")

    def current_balance(self):
        return self.balance

    def transaction_history(self):
        for trx in self.transactions:
            print(trx)
