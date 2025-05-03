# Find and return the largest number in a given list.
lst = [22,4,67,2,56,90,16,94]
largest = lst[0]
for i in range(1,len(lst)):
    if lst[i]>= largest:
        largest = lst[i]
print("largest number is " ,largest)
