with open("text.txt","r") as file:
    lines = file.readlines()
    longest=0
    for i in range(0,(len(lines))):
        if len(lines[i])>=longest:
            longest = len(lines[i])
        else:
            continue
print(longest)
    