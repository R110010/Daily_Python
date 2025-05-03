# Use list comprehension to create a list of squares of even numbers from 1 to 20.
lst =[n**2 for n in range(1,21) if n%2==0]
#lst=[n*n for n in range(1,21) if n%2==0]
print(lst)