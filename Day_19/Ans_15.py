# Implement a simple cache function using a dictionary.
# cube of a number
my_dict = {}
def func(n):
    if n in my_dict:
        res = my_dict[n]
        return f" Value from cache, cube ={res}"
    else:
        res = n**3
        my_dict[n]=res
        return f" new calculation, cube ={res} "
print(func(2))
print(func(4))
print(func(2))
print(func(3))
print(func(4))
print(func(5))
print(func(3))
print(func(2))
