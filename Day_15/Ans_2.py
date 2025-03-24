# Make a GET request to a public API (https://jsonplaceholder.typicode.com/todos/1).

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("all good" if response.status_code ==200 else f"response code : {response.status_code}")
