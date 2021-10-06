import json
import time
import os
import datetime
from urllib.request import urlopen

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

while True:
    now = datetime.datetime.now()
    print ('Steve\'s Crypto Prices as of', now.strftime("%Y-%m-%d %H:%M:%S"))
    print()
    with open('cryptos.txt', 'r') as file:
        for line in file:
            line = line.strip('\n')
            with urlopen("https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd".format(line)) as response:
                source = response.read()
                
            data = json.loads(source)
            crypto_price = json.dumps(data['{}'.format(line)]['usd'], indent=2)
            print('{}: ${}'.format(line, crypto_price))
        time.sleep(30)
        cls()

