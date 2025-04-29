# Check if two strings are equal ignoring cases
s1 = "this is a test string"
s2 = "this is a test string"

if s1.lower().strip() == s2.lower().strip():
    print(" both the string are the same")
else:
    print(" both the string are not same")