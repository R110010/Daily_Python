# function with default argument
def greet(name, msg="Good morning"):
    return (f" Hello, {name} Good morning")
print(greet(input("Please input your name :")))