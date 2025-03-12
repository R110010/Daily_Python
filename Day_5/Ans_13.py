# sum of digits of a number
n = int(input("Enter a number: "))
sum=0
while n>0:
    last_number= n%10
    sum= sum+last_number
    n=n//10
print(sum)