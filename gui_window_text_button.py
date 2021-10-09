import datetime
now = datetime.datetime.now()
import PySimpleGUI as sg

# sg.Window(title="Hello World", layout=[[]], margins=(150,250)).read()

layout = [
    [sg.Text("Hello from PySimpleGUI \n more \n more \n more")],
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("Demo", layout)

# create an event loop
while True:
    event, values = window.read()

    # end program if user closes the window or presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
