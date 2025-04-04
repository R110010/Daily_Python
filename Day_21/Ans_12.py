# Find the intersection of two lists (common elements).
lst1 = [9,7,5,2,12,11]
lst2 = [9,88,5,32,12,7]
lst3 = list(filter(lambda x:x in lst1,lst2))
print(lst3)