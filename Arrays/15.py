# Move all zeros to end of array.
arr = [0,1,0,2,0,3,0,4,0,5,6]
def move_zero(x):
    k = 0
    n= len(x)
    for i in range(n):
        if x[i]!=0:
            x[k]=x[i]
            k+=1 
    for j in range(k,n):
        x[j]=0
    return x
print("original list :",arr)
print("Modified list ",move_zero(arr))
