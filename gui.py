import PySimpleGUI as sg
from api_get_data import get_curr_usage

# All the stuff inside your window.

curr_usage = get_curr_usage()

first_name = curr_usage["user"]["first_name"]
last_name = curr_usage["user"]["last_name"]
curr_usage_kW = curr_usage["usage_kW"]
curr_level = curr_usage["level"]
cents_per_hr = curr_usage["cents_per_hr"]

layout = [  [sg.Text('Hi {}'.format(first_name))],
            [sg.Text('Your current usage level is {}'.format(curr_level))],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]



# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
