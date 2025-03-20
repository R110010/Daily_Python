# Catch an exception when trying to convert a string to an integer.
try:
    num =int(input(" enter a valid number :"))
    print("you entered",num)
except Exception as e:
    print(" please enter a valid interger ")