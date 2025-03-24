# use Header in an API requests
import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Content-Type": "application/json"
}
data = {
    "title": "Hello user",
    "body": "This is a test for content type",
    "userId": 1
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
