# Write a list of names to a file.

names =["ravi","nitin","rohit","shubho"]
try:
    with open("my_text.txt","w") as file:
        for name in names:
            file.write("\n"+name)
    print("File written successfully.") 
except:
    print(" somthing went wrong.")
