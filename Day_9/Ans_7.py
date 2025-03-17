# function to find factorial
def fact(num):
    factorial= 1
    while num>0:
        factorial = factorial*num
        num -=1
    return factorial
print(fact(int(input("Enter a number :"))))
    