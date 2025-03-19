# write list of fruits into a file
fruits = ["amla","kiwi","grapes","pear"]
with open("text.txt","a") as file:
    for fruit in fruits:
        file.write("\n"+fruit)
with open("text.txt","r") as f:
    print(f.read())