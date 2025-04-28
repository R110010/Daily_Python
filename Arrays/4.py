# Sort an unsorted array using bubble sort.
arr = [3,35,72,2,24,57,21,5,32,76]
def bubble_sort(x):
    
    for i in range(0,len(x)):
        for j in range(0,(len(x)-i)-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x
res = bubble_sort(arr)
print(res)