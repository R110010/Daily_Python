#
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposited {amount} New balance: {self.__balance}")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f" Withdrawn {amount} Remaining balance: {self.__balance}")
        elif amount > self.__balance:
            print(" Insufficient balance")
        else:
            print(" Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Rahul Sharma", 5000)
account.deposit(2000)
account.withdraw(3000)
account.withdraw(6000)
print(f" Current Balance: {account.get_balance()}")