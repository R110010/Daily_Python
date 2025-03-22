#Use super() to call parent class methods.
class Vehicle:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
    def speed(self):
        print("this is class Vehicle method ")
    def display_details(self):
        print(f"Brand : {self.brand}  Model :{self.model} color :{self.color}")
class Car(Vehicle):
    def __init__(self,brand,model,color,fuel):
        super().__init__(brand,model,color)
        self.fuel = fuel
    def speed(self):
        super().speed()
        print("this is class Car method")
    def display_details(self):
        super().display_details()
        print("Fuel :",self.fuel)
        
    
c1 = Car("Tata","Nexon","Olive","petrol")
c1.speed()
c1.display_details()