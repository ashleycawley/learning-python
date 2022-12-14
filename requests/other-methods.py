#!/usr/bin/env python3

import requests

url = 'https://httpbin.org/'

## Trying POST:
response = requests.post(url + 'post', data={'key': 'value'})
print("response:", response, "\n")
print("headers:", response.headers, "\n")
print("headers (content-type):", response.headers['content-type'], "\n")

## Trying PUT:
response = requests.put(url + 'put', data={'key': 'value'})
print("response:", response, "\n")

## Trying DELETE:
## Trying PUT:
response = requests.delete(url + 'delete')
print("response.status_code:", response.status_code, "\n")