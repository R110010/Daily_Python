with open("text.txt","a") as file:
    file.write("\nWelcome to Python!")

with open("text.txt","r") as f:
    content = f.read()
    print(content)


