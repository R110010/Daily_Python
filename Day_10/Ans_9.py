with open("text2.txt","r") as file:
    content = file.read()
    count = 0
    if "Python" in content:
        count +=1
print(f"the word Python occured {count} times")
