# Create a Person class and Employee subclass with an extra attribute salary.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f"Person details = Name : {self.name} Age : {self.age}")
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def display_details(self):
        super().display_details()
        print(" Salary :",self.salary)
e1 = Employee("Nitin",25,30000)
e1.display_details()