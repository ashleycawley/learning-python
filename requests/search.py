#!/usr/bin/env python3

import requests

# Search GitHub's Repos
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'bookstack'},
)

# Inspect some attributes of the repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repo name: {repository["name"]}')
print(f'Repo Description: {repository["description"]}')