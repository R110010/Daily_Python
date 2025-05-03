# find the seconf largest element in a list
lst=[2,2,2,2,2,2]
#lst = [2,4,5,73,56,79,24,90]
def find_second_largest(lst):
    
    if len(lst)<2:
        return None
    first = lst[0]
    second = float('-inf')
    count =0
    for num in lst:
        if first==num:
            count+=1
            if count==len(lst):
                return
        else:
            break
    count =0
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first<num<second:
            second = num
        else:
            continue
    return second
    
res = find_second_largest(lst)
print(res)