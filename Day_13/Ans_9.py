# Implement a Bank class with a method interest_rate() and override it in SavingsAccount.
class Bank:
    rate = 7
    def __init__(self,name):
        self.name = name
    def interest_rate(self):
        print(" default rate :",{Bank.rate})
    def display(self):
        return f"Name :{self.name}   rate of interest ={self.rate}"
class SavingAccount(Bank):
    rate = 6
    def interest_rate(self,name):
        SavingAccount.rate = 6

b1 = Bank("Bank of Busan")
print(b1.display())
a1 = SavingAccount("Wizard Bank")
print(a1.display())