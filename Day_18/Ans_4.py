# Catch multiple exceptions in a single block.

try:
    num1 = int(input(" enter the first number :"))
    num2 = int(input(" enter the second number :"))
    result = num1/num2
    print("result :",result)
except (ZeroDivisionError,ValueError) as e:
    print(" Error occured ",e)