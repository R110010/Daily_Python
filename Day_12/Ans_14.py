# Implement a class with a default parameter in the constructor.
class Student:
    schoolName = "Kendriya Vidyalaya, Kalimpong"
    def __init__(self,name,marks=40):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Name :{self.name}  Marks :{self.marks} School Name :{Student.schoolName}")
    def check_pass(self):
        if self.marks >=40:
            print(f" congrats {self.name}, you have passed.")
        else:
            print(f"Sorry {self.name} Better luck next time.")

s1 = Student("Griffin",99)
s1.display_details()
s1.check_pass()
s2 = Student("Slytherin",)
s2.display_details()
s2.check_pass()