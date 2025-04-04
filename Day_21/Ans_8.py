# Merge two lists and return a single sorted list.
lst1 = [9,7,5,2,12,11]
lst2 =["d","c","b","a","e","f"]
merged_list = sorted(lst1) + sorted(lst2) # merging first and then sorting will cause sorting error in numbers.
print(lst1)
print(lst2)
print(merged_list)