# Implement a Shape class and Rectangle subclass.
class Shape:
    print(" this is Shape class")
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth
        area = self.length * self.breadth
        
        print(" this is sub class Rectangle \n the area of rectangle os ",area)
r1 = Rectangle(5,6)
