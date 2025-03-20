# Use finally to ensure a message prints at the end of the program.
try:
    a=12
    b=0
    c=a/b
except ZeroDivisionError:
    print(" a number cannot be divided by zero")
finally:
    print(" this is printed from the finally block")