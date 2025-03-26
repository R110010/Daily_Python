# Implement multiple inheritance with a Vehicle class.
class Vechicle:
    def veh_traits(self):
        print(" class Vehicle properties")
        
class Car:
    def car_traits(self):
        print(" class CAr properties")

class Sedan(Vechicle,Car):
    pass
tigor = Sedan()
tigor.veh_traits()
tigor.car_traits()