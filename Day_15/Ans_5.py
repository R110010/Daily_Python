# Handle API errors using try-except.
import requests
url = "https://jsonplaceholde.typicode.com/todos/100" # wrong url
try:
    response = requests.get(url)
    print(response.status_code)
except Exception as e:
    print(" some error occured\n",{e})