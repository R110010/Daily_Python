# Search for an element (Linear Search)
arr = [3,35,72,2,24,57,21,5,32,76,1]
def linear_search(x,target):
    for i in range(len(x)):
        if x[i]==target:
            return ("target found at location :",i)
    return (" target does not exist")

print(linear_search(arr,1))
