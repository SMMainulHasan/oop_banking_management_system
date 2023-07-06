import time


class Transaction:
    def __init__(self, amount) -> None:
        self.amount = amount
        self.sender = None
        self.receiver = None
        self.type = None
        self.transaction_id = time.time()  # TODO:
        self.time = time.ctime(time.time())

    def __repr__(self) -> str:
        return f"--------------------------------------------------\nTransaction ID: {self.transaction_id}\nTime: {self.time}\nAmount: {self.amount}$\nType: {self.type}\nSender: {self.sender}\nReceiver: {self.receiver}\n--------------------------------------------------"
