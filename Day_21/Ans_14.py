# Find the missing number in a sequence from 1 to n.
lst = [1,2,3,4,5,7,8,9]

def find_missing(lst,n):
    total = n*(n+1)//2
    sum_lst = sum(lst)
    return total-sum_lst
res = find_missing(lst,(len(lst)+1))
print(res)