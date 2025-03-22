# Add a speed method in Vehicle and override it in Car.
class Vehicle:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
    def speed(self):
        print(" this is class Vehicle method ")
class Car(Vehicle):
    def speed(self):
        print("this is class Car method")
    pass
c1 = Car("Tata","Nexon","Olive")
c1.speed()