# Create multiple instances and modify attributes separately.
# Use instance variables and class variables in a class.
class Student:
    schoolName = "Kendriya Vidyalaya, Kalimpong"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Name :{self.name}  Marks :{self.marks} School Name :{Student.schoolName}")
    def check_pass(self):
        if self.marks >=40:
            print(f" congrats {self.name}, you have passed.")
        else:
            print(f"Sorry {self.name} Better luck next time.")
    def update_name(self,name):
        self.name = name
        print(" name updated successfully.")
    def update_marks(self,marks):
        self.marks=marks
        print("Marks updated successfully")

s1 = Student("Gryffindor",99)
s1.display_details()
s1.check_pass()
s1.update_name("Godrick Gryffindor")
s1.update_marks(98)
s1.display_details()
s2 = Student("Slytherin",35)
s2.display_details()
s2.check_pass()
s2.update_name("Salazar Slytherin")
s2.update_marks(41)
s2.check_pass()
s2.display_details()