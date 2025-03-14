3#Count ocurences of an element
my_list = ["first","second",3,4,5,"second",3,4,8,9,"second"]
search = input("enter the element to be searched :")
if search.isdigit():
    search= int(search)
count=0
for x in my_list:
    if x == search:
        count+=1
    else:
        continue
print(count)