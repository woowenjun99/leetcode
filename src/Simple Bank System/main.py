from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= 0 or account1 > len(self.balance) or account2 <= 0 or account2 > len(self.balance): return False
        if self.balance[account1 - 1] < money: return False
        return self.withdraw(account1, money) and self.deposit(account2, money)

    def deposit(self, account: int, money: int) -> bool:
        if account <= 0 or account > len(self.balance): return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account <= 0 or account > len(self.balance): return False
        if money > self.balance[account - 1]: return False
        self.balance[account - 1] -= money
        return True