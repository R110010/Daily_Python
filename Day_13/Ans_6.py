# Add a method in Employee to print salary.
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
    def salary_show(self):
        print(" Salary :",self.salary)
e1 = Employee("Nitin",25,30000)
e1.display_details()
e1.salary_show()