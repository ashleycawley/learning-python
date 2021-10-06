# Ashley's Crypto Ticker - Pulling data from CoinGecko's API

import requests
import json

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
#btc_price = json.loads(response)
print()
print(response.status_code)
print()
print(response)
#print(response)

print()