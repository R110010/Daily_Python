# Find the second largest number in a list.
lst = [10,22,4,67,2,56,90,16,94]
first, second = float("-inf"), float("-inf")
for num in lst:
    if num >first:
        second =first
        first = num
    elif first>num>second:
        second = num

print(second)