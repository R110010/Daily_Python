#Create a function that takes different objects and calls a common method.

class Dog:
    def speak(self):
        print("sound of Dog is  bark")
class Cat:
    def speak(self):
        print("sound of Cat is  meow")
        
def animal_sound(animal):
    animal.speak()
    
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)