import json
import requests
url = 'https://httpbin.org/post'

response = requests.post(url, data={'key':'value','brand':'Ford','year':'2007'})
print(response)

json_response = response.json()

print(json_response)

print(json_response['headers']['Content-Type'])

### Sending data as JSON
response = requests.post(url, json={'key': 'value', 'brand:': 'Ford', 'year': '2007'})
print(response)
json_response = response.json()
print(json_response)
print(json_response['headers']['Content-Type'], "\n")
print(json_response['json']['year'])