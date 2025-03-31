# Use filter() to find even numbers from a list.
num = [12,4,5,768,9,34,778,94,567,149]
result = filter((lambda x:x%2==0),num)
even_num = list(result)
print(even_num)