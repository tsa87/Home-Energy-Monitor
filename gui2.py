import PySimpleGUI as sg
import plotly.graph_objects as go
from api_get_data2 import get_curr_usage
from api_get_data2 import get_week_usage
from test_ground import get_time

# All the stuff inside your window.

name_array = []
percent_array = []

curr_weekly_usage = get_week_usage()
for appliance in curr_weekly_usage["appliances"]:
    name_array.append(appliance["name"])
    percent_array.append(appliance["percent"])

fig = go.Figure(data=[go.Pie(labels=name_array, values=percent_array)])
# fig.show()

curr_usage = get_curr_usage()
greetings = get_time()

first_name = curr_usage["user"]["first_name"]
last_name = curr_usage["user"]["last_name"]
curr_usage_kW = curr_usage["usage_kW"]
curr_level = curr_usage["level"]
cents_per_hr = curr_usage["cents_per_hr"]

main_menu = [
    [sg.Text("Dashboard", font=("Helvetica", 20))],
    [sg.Text('{} {}!'.format(greetings, first_name))],
    [sg.Text('Your current usage level is {}'.format(curr_level))],
    [sg.Text('Enter something on Row 2'), sg.InputText()],
    [sg.Button('Day'), sg.Button('Week')]
    [sg.fig.show()]

]

# Create the Window
window = sg.Window('Window Title', main_menu)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
