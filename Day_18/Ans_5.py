# Use finally to close a file after reading.
try:
    file = open("data.txt","r")
    data = file.read()
    print(data)
except Exception as e:
    print(" Error : ",e)
finally:
    file.close()
    print("file closed. ")