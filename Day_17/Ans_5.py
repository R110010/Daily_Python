# Use @property to make an attribute read-only.
class Person:
    def __init__(self,name,gender,age):
        self.name =  name
        self.gender = gender
        self.__age = age
    @property
    def age(self):
        return self.__age
p1 = Person("Gandalf","male",99)
print(p1.age)
