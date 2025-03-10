#max of three numbers
a = float(input("Enter first number :"))
b = float(input("Enter second number :"))
c = float(input("Enter third number :"))
if a>=b:
    if a>=c:
        print(f"{a} is the biggest number")
    else:
        print(f"{c} is the biggest number")
else:
    if b>=c: 
        print(f"{b} is the biggest number")
    else:
        print(f"{c} is the biggest number")
    