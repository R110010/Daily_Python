# Extract and print a list of users from an API response.
import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()
print("List of users : ")
for user in users:
    name=user["name"]
    print(name)
