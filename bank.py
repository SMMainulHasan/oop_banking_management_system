from users import Admin, General


class Bank:
    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
        self.__balance = 0
        self.__total_loan = 0
        self.__is_loan_available = True
        self.admins = []
        self.accounts = []

    def create_admin_account(self, user_name, email, bank_name):
        account = Admin(user_name, email, bank_name)
        self.admins.append(account)
        return account

    def create_General_account(self, user_name, email, bank_name):
        account = General(user_name, email, bank_name)
        self.accounts.append(account)
        return account

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, transaction):
        amount = transaction.amount
        if transaction.type == 'deposit':
            self.__balance += amount
        elif transaction.type == 'withdrawal':
            self.__balance -= amount
        elif transaction.type == 'loan':
            self.__balance -= amount
            self.__total_loan += amount

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
