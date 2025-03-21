# create a class that returns a formatted string
class Plants:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        return f"Name of the plant is {self.name}"
p1 = Plants("Kamini")
to_print =p1.display_name()
print(to_print)