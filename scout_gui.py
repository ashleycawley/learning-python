# Imports in libraries we will need to use
import json     # Used for manipulating JSON
import time     # Used for sleeping
import os       # Used for clearing the screen 
import datetime # Used for outputing the date and time
from urllib.request import urlopen # Used for retrieving the JSON from a URL
import PySimpleGUI as sg

source = """{"Servers":{"server51.group.net":"online","reseller2.host.com":"offline","svr.hostgroup.com":"online"},"Backups":{"Monday":"Present","Tuesday":"Present","Wednesday":"MISSING","Thursday":"Present","Friday":"Present"}}"""
data = json.loads(source)
servers = json.dumps(data, indent=2)
monday_backup = json.dumps(data['Backups']['Monday'], indent=2)
display_text = str(servers)

# sg.Window(title="Hello World", layout=[[]], margins=(150,250)).read()

layout = [
    [sg.Text("Scout Desktop GUI")],
    [sg.Text(display_text)],
    [sg.Text("\n")],
    [sg.Text("Backup Health: \n Monday's backup is:")],
    [sg.Text(monday_backup)],
    [sg.Text("\n")],
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("Scout v2.54 - GUI", layout)

# create an event loop
while True:
    event, values = window.read()

    # end program if user closes the window or presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
