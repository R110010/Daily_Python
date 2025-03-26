# Implement a constructor for automatic initialization.
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def get_info(self):
        return self.brand, self.model

c1 = Car("Toyota","Hilux")
c2 = Car("Maruti","Breeza")
c3 = Car("Tata","Nexon")
print(c1.get_info())
print(c2.get_info())
print(c3.get_info())