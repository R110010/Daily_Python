# Implement a class method using @classmethod.
class Vehicle:
    total_vehicles = 0
    def __init__(self):
        Vehicle.total_vehicles += 1

    @classmethod
    def get_total_vehicles(cls):
        return f"Total vehicles created: {cls.total_vehicles}"

car1 = Vehicle()
car2 = Vehicle()
car3 = Vehicle()

print(Vehicle.get_total_vehicles()) # calling through class
print(car1.get_total_vehicles()) # calling through objext
