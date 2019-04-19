import threading


class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.lock = threading.Lock()

    def get_balance(self):
        self.check_open_status(True)
        return self.balance

    def open(self):
        self.check_open_status(False)
        self.is_open = True


    def deposit(self, amount):
        self.check_open_status(True)
        if amount < 0:
            raise ValueError('Cannot deposit negative amount.')

        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        self.check_open_status(True)
        if amount < 0:
            raise ValueError('Withdrawl amount invalid or it exceeds balance.')

        with self.lock:
            self.balance -= amount
        if self.balance < 0:
            raise ValueError('Withdrawl amount invalid or it exceeds balance.')

    def close(self):
        self.check_open_status(True)

        with self.lock:
            self.is_open = False
            self.balance = 0

    def check_open_status(self, status):
        if status != self.is_open:
            raise ValueError('Account not accessible')
