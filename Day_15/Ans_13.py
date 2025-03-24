# Save API response data into a JSON file.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Content-Type": "application/json"
}
data = {
    "title": "Hello user",
    "body": "This is a test for content type",
    "userId": 1
}

def func_call():
    response = requests.post(url, json=data, headers=headers)
    return response.json()

api_call = func_call()
with open("response.json","w") as file:
    json.dump(api_call,file,indent=4)
print(" data saved to file successfully")
    