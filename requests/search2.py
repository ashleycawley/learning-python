#!/usr/bin/env python3

import requests

# Search GitHub's Repos
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'bookstack'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}
)

# Inspect some attributes of the repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Text Matches: {repository["text_matches"]}')
