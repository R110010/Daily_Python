# Fetch weather data from OpenWeatherMap API and display it.
import requests
import json
url = "https://api.openweathermap.org/data/2.5/weather"

api_key = "5bfa10f8ecc572532a95dd430d1ee5d0"
params = {
        'q': "Kalimpong",
        'appid': api_key,
        'units': 'metric'
    }
response = requests.get(url,params=params)
print(response.status_code)
data = response.json()
print(json.dumps(data,indent=4))
