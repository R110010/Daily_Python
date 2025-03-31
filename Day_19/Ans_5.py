# Implement a function to check for prime numbers using filter().
def is_prime(n):
    if n<2:
        return False
    for i in range(2,(int(n**0.5)+1)):
        if n%i==0:
            return False
        else:
            return True
        
number = list(range(1,32))
result =list(filter(is_prime,number))
print(result)