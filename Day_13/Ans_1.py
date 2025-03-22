# Create a Vehicle class and Car class that inherits it.

class Vehicle:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
class Car(Vehicle):
    pass