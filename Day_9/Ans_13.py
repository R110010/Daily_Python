# function to count number of vowels in a string
def vowel_count(my_strng):
    count=0
    for x in my_strng:
        if x in ("a","e","i","o","u"):
            count+=1
        else:
            continue
    return count
my_strng = input("enter a string :")
print("number of vowels in the string is",vowel_count(my_strng))