# Count occurrences of a given element
arr = [3,35,72,2,24,57,21,5,32,76,1,2,2,2]
def count_occurance(x,target):
    count = 0
    for i in range(len(x)):
        if x[i]==target:
            count+=1
    return target,count
num = int(input("enter the element to be searched : "))
target,count = count_occurance(arr,num)
print(f"{target} has occured {count} times.")