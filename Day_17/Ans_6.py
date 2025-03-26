# Create a subclass ElectricCar that inherits from Car.
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return self.brand, self.model, self.year
    
class ElectricCar(Car):
    pass

car1 = ElectricCar("Tata","Nexon EV",2024)
print(car1.get_info())