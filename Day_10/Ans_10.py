lst=[]
with open("blank.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        if line != "\n":
            lst.append(line)
        else:
            continue
print(lst)
with open("blank.txt","w") as f:
    for word in lst:
        f.write(word)