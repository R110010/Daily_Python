# Import a module inside a function instead of globally.
def square_num(num):
    from my_package import num_square
    return num_square(num)

result = square_num(4)
print("Square of number is :",result)