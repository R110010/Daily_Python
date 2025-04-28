#Find the second largest element
arr = [3,35,72,2,24,57,21,5,32,76,1]
def second_largest(x):
    for i in range(2):
        for j in range((len(x)-i)-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x[-2]
print("second largest element is :",second_largest(arr))
