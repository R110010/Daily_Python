# find the seconf largest element in a list
#lst=[1]
lst=[2,2,2,2,2,2]
#lst = [2,4,5,73,56,79,24,90]
def second_largest(lst):
    if len(lst)<2:
        return None
    first=second= float('-inf')
    for num in lst:
        if num>first:
            second = first
            first= num
        elif first>num>second:
            second = num
    return second if second!=float('-inf') else None      

res = second_largest(lst)
print(res)

