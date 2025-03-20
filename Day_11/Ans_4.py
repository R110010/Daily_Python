#Handle multiple exceptions (ZeroDivisionError, TypeError).
try:
    a=12
    b=0
    c = a/b
except ZeroDivisionError:
    print(" A number cannot be divided by zero")

try:
    a=4
    b="b"
    c = a/b
except TypeError:
    print(" a number cannot be divided by a string")