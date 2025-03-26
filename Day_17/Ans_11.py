# Define a private attribute and use getter/setter methods.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

person = Person("Ganga", 25)

print("Initial age ",person.get_age())
person.set_age(30)
print("New age ",person.get_age())
person.set_age(-5) #  invalid age
