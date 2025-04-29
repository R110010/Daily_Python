# Count vowels and consonants
import string
s = "this is a string"
s_mod = s.lower()
vowel = 0
consonent =0
for char in s_mod:
    if char in "aeiou":
        vowel+=1
    elif char in string.ascii_lowercase and char not in "aeiou":
        consonent +=1
print(f"Count of vowel is {vowel} and count of consonent is {consonent}.")