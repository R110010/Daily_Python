with open("text2.txt","r") as file:
    content = (file.read()).split()
    count = len(content)
print("number of words in the file is:",count)
