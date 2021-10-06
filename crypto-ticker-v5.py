# Imports in libraries we will need to use
import json     # Used for manipulating JSON
import time     # Used for sleeping
import os       # Used for clearing the screen 
import datetime # Used for outputing the date and time
from urllib.request import urlopen # Used for retrieving the JSON from a URL

# Function for clearing the screen and previous prices on Windows or Linux (cross-platform)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls() # Clears the screen

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
            print()
        time.sleep(30)
        cls() # Clears the screen