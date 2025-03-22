# Override a method in the Dog class.
#Implement a class hierarchy: Animal -> Dog.
class Animal:
    def __init__(self,species):
        self.species = species
    def display(self):
        print( " Species of Animal :",self.species)
class Dog(Animal):
    def __init__(self,species,color,weight):
        super().__init__(species)
        self.color = color
        self.weight = weight
    def display(self):
        print(f"color of the Dog is {self.color} and its weight is {self.weight}kg")
d1 = Dog("Dog", "Chocolate", 6)
d1.display()
        