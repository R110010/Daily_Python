# Add a method get_info() to return car details.
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return self.brand, self.model, self.year
