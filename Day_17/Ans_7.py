# Override a method in the subclass.
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return self.brand, self.model, self.year
    
class ElectricCar(Car):
    def get_info(self):
        return self.brand, self.model

car1 = ElectricCar("Tata","Nexon EV",2024)
print(car1.get_info())