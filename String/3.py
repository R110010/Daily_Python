# Check if a string is palindrome
s = "Radar"
s_mod = s.strip().lower()
s_rev = s_mod[::-1]
if s_mod==s_rev:
    print( " String is a palindrome ")
else:
    print(" String is not a plaindrome ")