#check if element exists in list 
my_list = ["first","second",3,4,5,"second",3,4,8,9,"second"]
search = input("enter the element to be searched :")
if search.isdigit():
    search= int(search)
else:
    pass
if search in my_list:
    print(f"Element '{search}' found")
    

