# Rotate a list to the right by k positions.
lst =["a","b","c","d","e","f"]
def rotate_lst(lst,k):
    if not list:
        return lst
    k = k%len(lst)
    new_lst = lst[-k:] + lst[:-k]
    return new_lst
res = rotate_lst(lst,5 )
print(res)

