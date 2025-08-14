from threading import RLock
from typing import List

class Bank:
    class Account:
        def __init__(self, balance: int):
            self.balance = balance
            self.lock = RLock()
        
        def deposit(self, money: int) -> bool:
            if money < 0:
                return False
            with self.lock:
                self.balance += money
            return True
        
        def withdraw(self, money: int) -> bool:
            if money < 0:
                return False
            with self.lock:
                if self.balance < money:
                    return False
                self.balance -= money
            return True

    def __init__(self, balance: List[int]):
        self.accounts = [self.Account(b) for b in balance]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self.check_is_valid_account(account1) and 
                self.check_is_valid_account(account2) and
                money >= 0):
            return False
        
        acc1 = self.get_account(account1)
        acc2 = self.get_account(account2)

        # Lock both accounts to avoid race conditions
        first, second = (acc1, acc2) if account1 < account2 else (acc2, acc1)

        with first.lock, second.lock:
            if acc1.balance < money:
                return False
            acc1.balance -= money
            acc2.balance += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.check_is_valid_account(account):
            return False
        return self.get_account(account).deposit(money)

    def withdraw(self, account: int, money: int) -> bool:
        if not self.check_is_valid_account(account):
            return False
        return self.get_account(account).withdraw(money)

    def check_is_valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.accounts)
        
    def get_account(self, account: int) -> Account:
        return self.accounts[account-1]
