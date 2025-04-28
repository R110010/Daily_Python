#Find the maximum and minimum element in an array
arr = [3,35,72,2,24,57,21,5,32,76,1]
def find_max(x):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            largest = x[i]
        else:
            largest = x[i+1]
    return largest
def find_min(x):
    for i in range(len(x)-1):
        if x[i]<x[i+1]:
            smallest = x[i]
        else:
            smallest = x[i+1]
    return smallest       
print("largest number in the array ",find_max(arr))
print("smallest number in the array ",find_min(arr))
