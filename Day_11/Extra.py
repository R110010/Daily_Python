# count frequency of alphabets in a string
text = " this is the string under test."
my_dict ={}
for char in text:
    if char.isalpha():
        char=char.lower()
        if char in my_dict:
            my_dict[char]+=1
        else:
            my_dict[char]=1
print(my_dict)