# function to check for even number
def even_checker(num):
    if num!=0:
        if num%2==0:
            return ("number is an even number")
        else:
            return ("number is an odd number")
    else:
        return ("number is zero")
print(even_checker(int(input("enter a number :"))))