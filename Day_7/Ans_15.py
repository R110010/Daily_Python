# check for palindrome
s = input("Enter a string: ")
s_clean = ''.join(char.lower() for char in s if char.isalnum())

if s_clean == s_clean[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
