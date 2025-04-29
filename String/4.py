# find the first non repeating character.
s = "this is a test string"
s_mod = s.lower()
def first_non_repeating(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    for char in s:
        if freq[char]==1:
            return char,freq
    return None
print(first_non_repeating(s_mod))
