# Add a method to check if the student has passed (marks >= 40).
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Name :{self.name}  Marks :{self.marks}")
    def check_pass(self):
        if self.marks >=40:
            print(f" congrats {self.name}, you have passed.")
        else:
            print(f"Sorry {self.name} Better luck next time.")

s1= Student("Griffin",99)
s1.display_details()
s1.check_pass()