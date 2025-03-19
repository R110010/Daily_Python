with open("text2.txt","r") as file:
    content = file.read()
updated_content = content.replace("Hello","hi")
with open("text2.txt","w") as f:
    f.write(updated_content)
    print("Hello replaced with Hi")