# Implement a method to track the total number of objects created.

class Vechicle:
    object_counter=0
    def __init__(self):
        Vechicle.object_counter+=1
    def veh_traits(self):
        print(" class Vehicle properties")
        
class Car:
    def car_traits(self):
        print(" class Car properties")

class Sedan(Vechicle,Car):
    pass
tigor = Sedan()
tigor.veh_traits()
tigor.car_traits()
print(" total number of objects created :",Vechicle.object_counter)