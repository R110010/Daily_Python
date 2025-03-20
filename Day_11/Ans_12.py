# handle exception inside a finction
def func(a,b):
    try:
        c = a/b
        return c
    except Exception as e:
        return e
    
print(func(2,4))
print(func(2,0))
print(func(4,7))