#Check if the array is sorted or not
arr = [1,2,3,4,5,6,7,8,9,1]
def check_sorted(x):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            return (" arrary is not sorted")
    return ("array is sorted")
print(check_sorted(arr))