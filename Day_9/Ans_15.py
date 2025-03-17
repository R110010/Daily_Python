#function to print largest from a list
def largest_element(my_list):
    largest = 1
    for i in range(0,len(my_list)):
        if my_list[i]>largest:
            largest = my_list[i]
            i+=1
        else:
            continue
    return largest
my_list= [33,44,76,34,97,34,70,101]
print(largest_element(my_list))
