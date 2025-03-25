# append a list to a file.

fruits = ["amla","kiwi","grapes","pear"]
try:
    with open("my_text.txt","a") as file:
        for fruit in fruits:
            file.write("\n"+fruit)
    print("File written successfully.") 
except:
    print(" somthing went wrong.")
