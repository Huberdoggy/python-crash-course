import PySimpleGUI as sg
import os, re

def ask_city_or_zip():
    sg.theme('Dark Tan Blue')
    layout = [ [sg.Button('Seach by City/State')], [sg.Button('Search by Zip Code')] ]
    return layout


def draw_zip_window():
    cwd = os.getcwd()
    fname = 'sunny.png'
    im = f"{cwd}/images/{fname}"  # concat path from working dir plus fname
    sg.theme('Dark Tan Blue')
    layout = [[sg.Image(im, size=(300, 300), pad=(100, 0))],
              [sg.Text('Enter the 5 Digit Zip Code'), sg.InputText(size=(5, 1))],
              [sg.Button("Search Zip", pad=(20, 20), size=(20, 1)),
               sg.Button("Exit", pad=(20, 20), size=(20, 1))]]
    return layout

def draw_main_window():
    cwd = os.getcwd()
    fname = 'sunny.png'
    im = f"{cwd}/images/{fname}"  # concat path from working dir plus fname
    sg.theme('Dark Tan Blue')
    layout = [[sg.Image(im, size=(300, 300), pad=(100, 0))],
              [sg.Text('Enter the city name'), sg.InputText(size=(20, 1))],
              [sg.Text('Enter the state code'), sg.InputText(size=(5, 1))],
              [sg.Button("Search Location", pad=(20, 20), size=(20, 1)),
               sg.Button("Exit", pad=(20, 20), size=(20, 1))]]
    return layout


def determine_image(dict_value):
    cwd = os.getcwd()
    im = f"{cwd}/images/" # base folder for images
    if 'rain' in dict_value or 'drizzle' in dict_value:
        f_name = 'rain.png'
    elif 'cloud' in dict_value or 'fog' in dict_value or 'mist' in dict_value:
        f_name = 'clouds.png'
    else:
        f_name = 'sunny.png' # just default for the time being
    im += f_name
    return im

def weather_data_window(city_name, j_dict, im):
    layout = [ [sg.Image(im, size=(200, 200), pad=(100, 0))],
              [sg.Text(f"Current weather for {str(city_name).title().strip()}")],
              [sg.Text(f"Temperature in Fahrenheit: {str(j_dict['temp'])}")],
              [sg.Text(f"Atmospheric pressure (in psi): {j_dict['pressure']:.1f}")],
              [sg.Text(f"Humidity: {str(j_dict['humidity'])}%")],
              [sg.Text(f"Forecast is showing: {str(j_dict['description'])}")],
              [sg.Button('New Query'), sg.Button('Exit')] ]
    return layout

def show_error_window():
    layout = [ [sg.Text('An error has occured!')], [sg.Text('Please check your input and try again')],
               [sg.Button('Ok')] ]
    # return layout
    window = sg.Window('ERROR', layout)
    event, values = window.read()
    if event == 'Ok' or event == sg.WIN_CLOSED:
        window.close()

def check_reg_city_state(pattern_dict, input_var1, input_var2):
    if not (re.fullmatch(pattern_dict.get('loc_pattern', 'empty'), input_var1)
            and re.fullmatch(pattern_dict.get('state_pattern', 'empty'), input_var2)):
        return False
    else:
        return True

def check_reg_zip(pattern_dict, input_var1):
    if not (re.fullmatch(pattern_dict.get('zip_pattern', 'empty'), input_var1)):
        return False
    else:
        return True