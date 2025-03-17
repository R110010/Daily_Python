# function to return sum of three functions
def sum_three(num1,num2,num3):
    sum= num1+num2+num3
    return sum
num1,num2,num3 = map(int,input("enter the three numbers seperated by space :").split())
print(sum_three(num1,num2,num3))
