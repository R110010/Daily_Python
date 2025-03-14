#reversing a list by modifying the original list
numbers = [1,9,4,8,2,6]
numbers.reverse()
print(numbers)

# creating a new list and modifying it
numbers = [1,9,4,8,2,6]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)

# using slicing method
numbers = [1,9,4,8,2,6]
reversed_numbers = numbers[::-1]
print(reversed_numbers)