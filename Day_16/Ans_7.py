# Read and parse a JSON file.
import json
with open("data.json","r") as file:
    data = json.load(file)
    print(data)