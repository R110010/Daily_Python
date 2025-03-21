# Create a class BankAccount with balance attribute.
class BankAccount:
    def __init__(self,balance):
        self.balance= balance
    def display_details(self):
        print(" Balance ", self.balance)
b1= BankAccount(123456789)
b1.display_details()
