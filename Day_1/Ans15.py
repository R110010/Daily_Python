# write a script to print "Python is Fun!" 10 times.

# Using Only print function
print("1. Using Only Print function")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")
print("Python is Fun!")


# using String Multiplication
print("\n2. Using string multiplication")
print(("Python is Fun!\n")*10)

# using for loop
print("\n3. Using for loop") 
for i in range(10):
    print("Python is Fun!")

# Using List Comprehensions
print("\n4. Using List Comprehensions")
print_10 = ["Python is Fun!" for x in range(10)]
print(print_10)


# Using While loop
print("\n5. Using while loop")
i=0
while i<10:
    print("Python is Fun!")
    i+=1

#Using function (Recursive call)
print("\n6. Using function recursively")
def print_10(num):
    if num > 0:
        print("Python is Fun!")
        print_10(num-1)
print_10(10)