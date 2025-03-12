#count number of digits
num = int(input("Enter a number: "))
count = 0
n = abs(num)

if num == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print(f"Total digits in {num} is {count}")
