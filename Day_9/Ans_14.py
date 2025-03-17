# recursive function to returna fibinacci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the nth position of Fibonacci number: "))
print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
