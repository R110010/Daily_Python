# Check if two strings are anagrams
sa = "mug"
sb = "gum"
def anagram_checker(sa,sb):
    if len(sa)!=len(sb):
        return False
    if sorted(sa)==sorted(sb):
        return True
    else:
        return False
    
print(anagram_checker(sa,sb))