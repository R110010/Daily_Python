# factorial of a number
num =int(input("enter a number to find its factorial :"))
factorial =1
for i in range(1,num+1):
    factorial *=i
print(f"factorial of {num} is {factorial}")