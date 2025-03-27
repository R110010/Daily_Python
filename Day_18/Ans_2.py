# Use try-except to handle a missing file.

try:
    with open("nofile.txt","r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("opps !!! looks like the file is not present")