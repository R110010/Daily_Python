# Count the number of lines in a file.
with open("my_text.txt","r") as file:
    lines = file.readlines()
    count = len(lines)

print(count)