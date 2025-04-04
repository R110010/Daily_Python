# Remove all duplicate elements from a list.
# using dict.fromkeys() methos preserves order of list.
lst =["a","b","c","d","e","f","a","b","b","d","c"]
new_lst = list(dict.fromkeys(lst))
print(new_lst)

# this method does not preserve order.
lst2 = ["g","h","i","g","h","i","j"]
temp = set(lst2)
new_lst2 = list(temp)
print(new_lst2)