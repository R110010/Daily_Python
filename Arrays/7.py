#Calculate the sum of all elements
arr = [3,35,72,2,24,57,21,5,32,76,1]
def sum_array(x):
    sum = 0
    for num in x:
        sum = sum + num
    return sum
print("sum of the elements of array : ", sum_array(arr))