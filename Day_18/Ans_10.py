# Use assert statements to validate input.
def age(age):
    assert age>=0,"Age cannot be negative"
    print("age is",age)

age(12)
age(0)
age(-14)