#Handle an exception when trying to divide a number by a string.
try:
    a=4
    b="f"
    c=a/b
except TypeError:
    print(" please enter valid intergers ")