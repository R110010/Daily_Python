# make an API call from inside a function
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

def func_call():
    response = requests.post(url, json=data, headers=headers)
    return response

api_call = func_call()
print(api_call.status_code)
print(api_call.json())
