class MobileMoney:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Testing the application
account = MobileMoney(100000)   # Starting balance

account.deposit(50000)          # Add money
account.check_balance()

account.withdraw(30000)         # Withdraw money
account.check_balance()