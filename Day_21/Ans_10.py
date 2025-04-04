# Find the second largest number in a list.
lst = [10,22,4,67,2,56,90,16,94]
largest = 0
second_lar = 0
for i in range(0,len(lst)):
    if lst[i]> largest:
        second_lar =  largest
        largest = lst[i]
    elif largest >lst[i]> second_lar:
        second_lar = lst[i]
    
print("largest number is " ,largest)
print("second largest number is " ,second_lar)

