# Use reduce() to find the product of all numbers.
from functools import reduce
lst = [1,2,3,4,5]
result = reduce((lambda x,y:x*y),lst)
print(result)
