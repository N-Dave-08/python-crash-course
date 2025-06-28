import requests
import json

# http requests
res = requests.get("https://api.github.com")
print(res.status_code)

json_str = '{"name": "Sergio", "age": 29}'
data = json.loads(json_str)
print(data["age"])

# 2
d  = {"x": 1}
print(json.dumps(d))

# use case
url = "https://pokeapi.co/api/v2/pokemon/ditto"
res = requests.get(url)
data = res.json()
print(data["abilities"][0]["ability"]["name"])
