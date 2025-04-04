# Check whether a given list is sorted in ascending order.
#lst = [4,5,15,32,12,7]
lst = [1,2,3,4,5,6]
def check_asc(lst):
    for i in range(0,len(lst)):
        for j in range((i),len(lst)):
            if lst[i]>lst[j]:
                return(" list soeted is not in ascending order")
            
        else: 
            continue
    return (" list is not sorted in ascending order ")

res = check_asc(lst)
print(res)