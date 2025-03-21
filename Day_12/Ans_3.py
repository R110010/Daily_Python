# create multiple of car and print their details
# create a class Car with attributes brand and model and add a method to display its details.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print("brand :",(self.brand))
        print("model :",(self.model))
my_car1 = Car("mahendra","thar")
my_car2 = Car("toyota","hilux")
my_car1.display_info()
my_car2.display_info()
        