#Demonstrate multiple inheritance in Python.
class Vehicle:
    def vehicle_traits(self):
        print(" Vehicle Used for transportation ")
class Car:
    def car_traits(self):
        print(" Car used for transportation on land")
class Four_wheeler(Vehicle,Car):
    def four_wheeler_traits(self):
        print(" a four wheeled car is a vehicke used for land transportation ")
truck = Four_wheeler()
truck.vehicle_traits()
truck.car_traits()
truck.four_wheeler_traits()
