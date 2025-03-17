def prime_num(n):
    if n<=1:
        print("number cannot be less then 2")
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                print("its not a prime number")
                return
        print("its a prime number")
n = int(input("Enter a number to be checked for primness :"))
prime_num(n)