# Module 12: Working with APIs and JSON

## Overview
APIs let you interact with web services. JSON is a common data format for APIs.

---

## Making HTTP Requests
```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

## Parsing JSON
```python
import json
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)
print(data["name"])
```

---

## Mini Exercises
1. Use `requests` to get data from `https://api.github.com` and print the status code.
2. Convert a Python dictionary to a JSON string.

### Answers
```python
# 1
import requests
r = requests.get("https://api.github.com")
print(r.status_code)

# 2
import json
d = {"x": 1}
print(json.dumps(d))
```

---

## Real-World Use Case
Suppose you want to get weather data from an API:
```python
import requests
url = "https://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q=London"
response = requests.get(url)
data = response.json()
print(data["current"]["temp_c"])
``` 