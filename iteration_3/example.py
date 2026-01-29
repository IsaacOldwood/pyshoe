import requests

# GET request, returns HTML
r = requests.get("https://www.google.com")
print(r.text)

# GET request, returns JSON
r = requests.get("https://api.github.com/events")
print(r.status_code)
print(r.json())

# POST request, returns JSON
r = requests.post("https://httpbin.org/post", data={"key": "value"})
print(r.json())
