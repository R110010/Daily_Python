# Use query parameters in an API request.
import requests

url = "https://jsonplaceholder.typicode.com/posts/"

params = {
    "usedId":1,
    "id":5
}
response = requests.get(url,params=params)
print(response.url)
print(response.json())