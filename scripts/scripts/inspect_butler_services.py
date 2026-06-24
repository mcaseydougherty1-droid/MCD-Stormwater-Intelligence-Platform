import requests

URL = "https://geo.co.butler.pa.us/server/rest/services?f=json"

response = requests.get(URL, timeout=60)
response.raise_for_status()

data = response.json()

print(data.keys())
print(data)
