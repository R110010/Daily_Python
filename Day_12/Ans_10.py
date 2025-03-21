#Create a class Student with attributes name and marks.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Name :{self.name}  Marks :{self.marks}")

s1= Student("Griffin",99)
s1.display_details()