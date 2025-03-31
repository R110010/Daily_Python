# Use map() with multiple lists.
list1 = [2,3,4,5,6,7]
list2 = [9,2,5,3,7,8]
result = list(map(lambda x,y: x if x>=y else y,list1,list2))
print(result)