# Sort an array using selection sort.
arr = [3,35,72,2,24,57,21,5,32,76,1]
def Selection_sort(x):
    for i in range(0,len(x)-1):
        smallest = i
        for j in range(i+1,len(x)):
            if x[smallest] >x[j]:
                smallest=j
        x[i],x[smallest]=x[smallest],x[i]
    return x
           


res = Selection_sort(arr)
print(res)