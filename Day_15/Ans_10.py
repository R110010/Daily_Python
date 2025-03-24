# Check the response status code before processing the response.
import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print("List of users : ")
    for user in users:
        name=user["name"]
        print(name)
