#convert tuple into list modify it and convert it back to tuple
my_tuple = ("first","second",3,4,5)
print("tuple",my_tuple)
my_list = list(my_tuple)
print("List",my_list)
my_list.append("last")
print("modified list",my_list)
mod_my_tuple = tuple(my_list)
print("modified tuple",mod_my_tuple)