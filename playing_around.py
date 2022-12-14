# Imports in libraries we will need to use
import json     # Used for manipulating JSON
import time     # Used for sleeping
import os       # Used for clearing the screen 
import datetime # Used for outputing the date and time
from urllib.request import urlopen # Used for retrieving the JSON from a URL
import PySimpleGUI as sg

with urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd") as response:
    source = response.read()
    data = json.loads(source)
    crypto_price = json.dumps(data['bitcoin']['usd'], indent=2)
    display_text = str("bitcoin: ${}".format(crypto_price))

# sg.Window(title="Hello World", layout=[[]], margins=(150,250)).read()

layout = [
    [sg.Text("Steve's Bitcoin Ticker:")],
    [sg.Text(display_text)],
    [sg.Text("\n")],
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("Bitcoin", layout)

# create an event loop
while True:
    event, values = window.read()

    # end program if user closes the window or presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
