import json
import time
from urllib.request import urlopen

while True:

    with open('cryptos.txt', 'r') as file:
        for line in file:
            print(line)
            #time.sleep(60)



    with urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd") as response:
        source = response.read()

    data = json.loads(source)
    btc_price = json.dumps(data['bitcoin']['usd'], indent=2)
    print('Bitcoin: ${}'.format(btc_price))
    time.sleep(60)