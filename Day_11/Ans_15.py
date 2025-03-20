# Catch an AttributeError
try:
    x=10
    x.append(2)
    print(x)
except AttributeError:
    print(" there is an attribute error ")