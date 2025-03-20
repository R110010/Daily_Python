# Use else with try-except to execute code if no error occurs.
try:
    a=4
    b=4
    c=a/b
except TypeError:
    print(" please enter valid intergers ")
else:
    print(" Answer :", c)