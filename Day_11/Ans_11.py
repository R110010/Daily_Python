# Handle IndexError when accessing an empty list.
lst=[]
try:
    value =lst[2]
    print("value is ",value)
except IndexError:
    print(" index of list out of range.")