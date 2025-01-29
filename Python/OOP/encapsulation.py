class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}, New Balance: {self._balance}")

    def get_balance(self):
        return self._balance

# Creating an object
account = BankAccount("Alice", 5000)
account.deposit(2000)
print("Balance:", account.get_balance())
