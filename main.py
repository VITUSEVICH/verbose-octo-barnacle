class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("Баланс счета:", self.balance)


account = BankAccount(1000)
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()







