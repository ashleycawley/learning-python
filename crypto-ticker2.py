# Ashley's Crypto Ticker - Pulling data from CoinGecko's API
import requests
import json
import time

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

while True:
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    print()
    print('Status Code: ', response.status_code)
    print()
    jprint(response.json())
    time.sleep(30)