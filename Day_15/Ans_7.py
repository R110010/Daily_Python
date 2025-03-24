# Send data in JSON format in a POST request.
import requests
url = "https://jsonplaceholder.typicode.com/posts/"

try:
    data = {
        "title":"Sending a post request",
        "body":"this is a post request body",
        "userId":1001
    }
    response = requests.post(url,json=data)
    print(response.status_code)
    
except Exception as e:
    print(" somthing went wrong ",{e})
