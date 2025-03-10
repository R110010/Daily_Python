#Vowel checker
char = input("Enter a single alphabet: ")
char = char.lower()

if len(char) == 1 and char.isalpha():
    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f"{char} is a Vowel.")
    else:
        print(f"{char} is a Consonant.")
else:
    print("Please enter a single alphabet character.")
