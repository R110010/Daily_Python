# Raise a ValueError if age is negative.
def Age(num):
        if num<0:
            raise ValueError(" Age cnnot be negative")
        else:
            print(" your age is", num)
Age(12)
Age(0)
Age(-12)