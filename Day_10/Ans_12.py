with open("User_input.txt","w") as file:
    file.write(input("Write somthing in this file :"))
with open("User_input.txt","r") as f:
    f.seek(0)
    print("content of file :\n",f.read())
