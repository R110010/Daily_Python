# Demonstrate method overloading by using default arguments.
class Sum:
    def __init__(self):
        pass
    def total(self,a=0,b=0,c=0):
        return a+b+c
s1= Sum()
ss1 = s1.total(2,4)
print(ss1)
ss2 = s1.total(2,4,5)
print(ss2)