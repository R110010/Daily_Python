# Separate even and odd numbers from a list into two separate lists.
numbers =[1,23,57,23,78,24,78,356,94,25,9634,84568,2190]
even_lst =[]
odd_lst = []
for num in numbers:
    if num ==0:
        continue
    elif num%2==0:
        even_lst.append(num)
    else:
        odd_lst.append(num)
print("original list : ",numbers)
print("even number list :",even_lst)
print("odd number list : ",odd_lst)