import PySimpleGUI as sg
from api_get_data import get_curr_usage
from test_ground import get_time
from test_ground import get_color
# All the stuff inside your window.

curr_usage = get_curr_usage()

first_name = curr_usage["user"]["first_name"]
last_name = curr_usage["user"]["last_name"]
curr_usage_kW = curr_usage["usage_kW"]
curr_level = curr_usage["level"]
cents_per_hr = curr_usage["cents_per_hr"]

greetings = get_time()
curr_status_color = get_color(curr_level)


main_menu = [
            [sg.Text("Dashboard",font=("Helvetica", 20))],
            [sg.Text('{} {}!'.format(greetings, first_name))],
            [sg.Canvas(size=(20, 20), background_color=curr_status_color, key= 'canvas'),
                sg.Text('Current Usage Level: {}'.format(curr_level))],
            [sg.Button('Day')],
            [sg.Button('Week')],
            [sg.Button('Cancel')] ]



# Create the Window
win1 = sg.Window('Dashboard', main_menu)
win2_active = False
win3_active = False

while True:
    ev1, vals1 = win1.read()
    if ev1 == 'Day' and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Day')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Day', layout2)
        while True:
            ev2, vals2 = win2.Read()
            if ev2 is None or ev2 == 'Exit':
                win2.Close()
                win2_active = False
                win1.UnHide()
                break

    elif ev1 == 'Week' and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Week')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Week', layout2)
        while True:
            ev2, vals2 = win2.Read()
            if ev2 is None or ev2 == 'Exit':
                win2.Close()
                win2_active = False
                win1.UnHide()
                break

    elif ev1 == "Cancel":
        break
win1.close()


'''
layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text('', key='_OUTPUT_')],
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window 1', layout)
win2_active=False
while True:
    ev1, vals1 = win1.Read(timeout=100)
    if ev1 is None:
        break
    win1.Element('_OUTPUT_').Update(vals1[0])

    if ev1 == 'Launch 2'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
        [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.Read()
            if ev2 is None or ev2 == 'Exit':
                win2.Close()
                win2_active = False
                win1.UnHide()
                break

'''
