# Rotate a list to the left by k positions.
lst =["a","b","c","d","e","f"]
def rotate_left(lst,k):
    if not lst:
        return lst
    k = k%len(lst)
    new_lst = lst[k:] + lst[:k]
    return new_lst
ll =rotate_left(lst,5)
print(ll)