#Handle missing JSON keys without errors.
import json
json_data = '{"name":"Shobha","age":22}'
data = json.loads(json_data)
name = data.get("name","not present")
age = data.get("age","not present")
city = data.get("city","not present")
print(name)
print(age)
print(city)