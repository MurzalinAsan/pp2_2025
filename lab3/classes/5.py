class Account:
    owner = ""
    balance = 0

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    def withdraw(self, number):
        if self.balance > number:
            self.balance -= number
            return self.balance
        return "may not exceed the available balance"
    
owner = str(input())
balance = float(input())
amount = float(input())
thebalance = Account(owner, balance)
thebalance.deposit(amount)





        