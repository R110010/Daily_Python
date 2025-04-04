# Rotate a list to the right by k positions.
lst =["a","b","c","d","e","f"]
def rotate_lst(lst,k):
    k = k%len(lst)
    new_lst = lst[-k:] + lst[:-k]
    return new_lst
res = rotate_lst(lst,3)
print(res)

