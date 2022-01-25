#!/usr/bin/env python3

import requests

url = 'https://api.github.com/repos/ashleycawley/learning-python'

response = requests.get(url)

# Checking Status codes and behaving differently based on those:
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")

response.json()

def print_d(json):
    for key, value in json.items():
        print(f'{key} : {value}')

json_response = response.json()
# print_d(json_response) # Prints all JSON elements within the response using custom function defined above

#print(json_response['language']) # Retrieving one element from within the JSON response

print_d(response.headers) # Show response headers from the API Server
print("\n", response.headers['Content-Type']) # Shows the content type (ie. application/json)

# ================================

print("\n"+"Next set of experiments", "\n")

url2 = 'https://api.github.com/madlad'

response = requests.get(url2)

# Checking Status codes and behaving differently based on those:
if response.status_code == 200:
    print("Success!")
else:
    print("An error occurred.")

