# Pretty-print JSON data.
import json
my_dict = {"name": "Rongynoo",
           "age": 30}
with open("data.json","a") as file:
    file.write("\n")
    json.dump(my_dict,file, indent=4) # pretty print