with open("text.txt","r") as file:
    content = file.read()
with open("text2.txt","w") as file2:
    file2.write(content)
with open("text2.txt","r") as f:
    print("\ncontent of second file \n",f.read())