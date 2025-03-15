# check if string contains A and Z at start and end respt.
s = "A string to be tested for Z"
if s[0]=="A" and s[-1]=="Z":
    print(" string contains A at beginning and Z at the end")
elif s[0]=="A" and s[-1]!="Z":
    print("Only A is present")
elif s[0]!="A" and s[-1]=="Z":
    print("only Z present ")
else:
    print("Both A and Z not present")