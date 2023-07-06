import time


class Transaction:
    def __init__(self, amount) -> None:
        self.amount = amount
        self.sender = None
        self.receiver = None
        self.transaction_type = None
        self.transaction_id = time.time()  # TODO:
        self.time = time.ctime(time.time())
