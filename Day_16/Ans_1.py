# Open and read a text file.
try:
    with open("my_text.txt","r") as file:
        lines = file.readlines()
        print(lines)
except:
    print(" seems there are some errors")