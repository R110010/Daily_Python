# Extract and print a specific field from the API response.

import requests

url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(url)
print("all good" if response.status_code ==200 else f"response code : {response.status_code}")
data = response.json()
print(data)
print("user id :",data["userId"])