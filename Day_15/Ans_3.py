# Parse and print JSON response from an API.
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("all good" if response.status_code ==200 else f"response code : {response.status_code}")
data = response.json()
print(data)