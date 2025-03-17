# function that takes a list and returns the maximum element.
def lst_max(my_lst):
    greatest = 1
    for i in range(0,len(my_lst)):
        if my_lst[i]>greatest:
            greatest=my_lst[i]
        else:
            continue
    return greatest
        
my_lst=[2,5,7,9,16]
print("Biggest element in the list is",lst_max(my_lst))
    