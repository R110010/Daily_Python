# Delete an element by value without using inbuild functions.
arr = [1,2,3,4,5,6,7,8,9]
def delete_by_value(x,value):
    if value not in x:
        return (f"{value} not found in list.")
    n = len(x)
    k=0
    for i in range(n):
        if x[i]!= value:
            x[k]=x[i]
            k+=1
    return x[:k]
 

print(delete_by_value(arr,7)) 