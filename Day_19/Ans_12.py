# Implement a function that returns a lambda function.
def square_number():
    return lambda x:x**2
square =square_number()
print(square(6))