# Write a function using reduce() to find the largest number in a list.
from functools import reduce
lst = [1, 12, 8,3, 4, 5,12.0001]

lar_num = reduce(lambda x,y: x if x>=y else y,lst)
print(lar_num)