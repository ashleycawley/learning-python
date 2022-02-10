#!/usr/bin/env python3
import requests
from getpass import getpass

## Authentication Parameters are sent with: auth=
## The username and password are passed as a tuple
## the 'requests' library defaults to using "HTTP Basic" authentication scheme

url = 'https://api.github.com/user/repos'
headers = {"Authorization": "token e"}
response = requests.get(url, headers=headers)

print(response.status_code)
print(response)
print(response.content)