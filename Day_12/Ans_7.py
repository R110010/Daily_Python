# Create an object of BankAccount and perform operations.
class BankAccount:
    def __init__(self,balance):
        self.balance= balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        self.balance = self.balance - amount
    def display_details(self):
        print(" Balance ", self.balance)
# b1 is the object of BankAccount
b1= BankAccount(100000)
b1.display_details()
b1.deposit(25000)
b1.display_details()
b1.withdraw(1000)
b1.display_details()