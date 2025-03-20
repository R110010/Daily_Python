# function to make sure only positive numbers are passed
def positive(a):
    if a<0:
        raise ValueError(" number cannot be less then zero")
    else:
        return a
print(positive(1))
print(positive(0))
print(positive(-2))