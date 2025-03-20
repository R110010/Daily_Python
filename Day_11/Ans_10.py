# Use assert to check if a number is positive.
try:
    num = int(input(" enter a valid positive number :"))
    assert num >=0, "number must be positive"
    print( " you have entered",num)
except Exception as e:
    print(" error occured",e)
