# Implement a base class with a method that works differently in multiple subclasses.

class Sum:
    def total(self, a, b, c=0):
        return a + b + c

class AddTwo(Sum):
    def total(self, a, b, c=0):
        return a + b

class AddThree(Sum):
    def total(self, a, b, c=0):
        return a + b + c

s1 = AddTwo()
print("AddTwo:", s1.total(2, 3)) 

s2 = AddThree()
print("AddThree:", s2.total(2, 3, 4))  
