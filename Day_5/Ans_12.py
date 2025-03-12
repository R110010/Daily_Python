#fibonacci series
n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")
while count < n:
    print(a, end=' ')
    next_term = a + b
    a = b
    b = next_term
    count += 1
