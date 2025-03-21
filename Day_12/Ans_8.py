# Implement a Person class with name and age.
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f"Name :{self.name}  Age :{self.age}")


name, age = [ x.strip() for x in  input("enter yout name and age seperated by a comma :").split(",")]

p1 =person(name,age)
p1.display_details()
