# Create multiple objects and print their details.
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return self.brand, self.model, self.year

c1 = Car("Toyota","Hilux",2024)
c2 = Car("Maruti","Breeza",2022)
c3 = Car("Tata","Nexon",2019)
print(c1.get_info())
print(c2.get_info())
print(c3.get_info())