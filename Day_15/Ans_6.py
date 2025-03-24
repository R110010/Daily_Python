# Make a POST request to an API.
import requests
url = "https://jsonplaceholder.typicode.com/todos/"

try:
    data = {
        "title":"Learning python",
        "body":"this is a post request body",
        "userId":101
    }
    response = requests.post(url,json=data)
    print(response.status_code)
    
except Exception as e:
    print(" somthing went wrong ",{e})

