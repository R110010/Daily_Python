import os
if os.path.exists("text.txt") ==True:
    with open("text.txt","r") as file:
        print(file.read())