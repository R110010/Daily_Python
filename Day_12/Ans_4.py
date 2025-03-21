# use __init__ constructor to initialise
class Car:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
    def display_details(self):
        print(f" Brand :{self.brand}  model :{self.model}  color :{self.color}")

c1= Car("toyota","hilux","Green")
c1.display_details()
