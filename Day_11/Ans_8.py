# function to handle a file ot found error.
try:
    with open("file.txt","r") as file:
        print(file.readline())
except FileNotFoundError:
    print(" file does not exist ")