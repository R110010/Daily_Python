def divide(a,b):
    if b==0:
        raise ValueError(" cannot divide by zero")
    else:
        return a/b
divide(10,2)
divide(10,0)