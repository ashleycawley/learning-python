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
    str(response)
    print('Data Type of \'response\' : ', type(response))
    print()
    print('Status Code: ', response.status_code)
    print()

    sample_json= '{"bitcoin":{"usd":54356}}'

    # jprint(response.json())

    print(json.loads(sample_json[0].text))

    time.sleep(30)