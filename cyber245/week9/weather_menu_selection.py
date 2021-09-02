import re, sys
from time import sleep
import PySimpleGUI as sg
import pyowm.commons.exceptions
from pyowm import OWM
from pyfiglet import Figlet
from termcolor import cprint
from open_weather_cli import choice_one
import secrets

mod_paths = {'week6': '/home/huberdoggy/python-projects/python-crash-course/cyber245/week6', }
from cli_functions import add_to_path as atp, compile_patterns, make_menu as mm

atp(mod_paths)  # insert my other modules in $PYTHONPATH.. using lst for room to expand if needed
from cars_and_trucks import format_main_menu as f_m, screen_clear as s_c

# Simple lambda functions to quickly convert print call color for 'x' argument provided
print_green = lambda x: cprint(x, 'green')
print_red = lambda x: cprint(x, 'red')

f = Figlet(font='standard')
welcome_str = "Kyle\'s Weather Retrieving App"
opts_lst = ['Run program from the CLI', 'Run the GUI experience', 'Quit']
farewell = "Thank you for using the app. Good-bye!"
valid_int = False
reg_patterns = {
    'menu_sel_pattern': '^[1-3]{1}',
}
compile_patterns(reg_patterns)  # I outsourced this to its own function to quickly compile all patterns in the list
# Make the main program menu by passing indexes of 'opts_lst' to my 'make_menu' function
options_dict = mm(opts_lst[0], opts_lst[1], opts_lst[2])

while not valid_int:
    f_m(welcome_str, options_dict)
    choice = input("=> ")
    if re.fullmatch(reg_patterns.get('menu_sel_pattern'), choice):
        valid_int = True
        choice = int(choice)  # After safely passing check, this can convert
        if choice == 1:
            s_c()
            still_running = choice_one()
            if still_running:
                valid_int = False  # repeat the menu selection loop from the top...
        elif choice == 2:
            owm = OWM(secrets.api_key)  # Initialize OWM wrapper with my API key
            manager = owm.weather_manager()
            layout = [[sg.Text('Enter the city name'), sg.InputText()],
                      [sg.Button("Search City"), sg.Button("Exit")]]  # Create the window
            window = sg.Window(welcome_str, layout)
            # Create an event loop
            while True:
                event, values = window.read()
                # End program if user closes window or
                # presses the Exit button
                if event == "Exit" or event == sg.WIN_CLOSED:
                    sys.exit(0)  # Just end it
                else:
                    break  # Continue onto the next step

            try:
                observe = manager.weather_at_place(values[0])
            except pyowm.commons.exceptions.NotFoundError:
                layout = [[sg.Text('Error, location not recognized. The program will now exit')],
                          [sg.Button('OK')]]
                window = sg.Window(welcome_str, layout)

                while True:  # Pops a new box that just has the error and an 'OK' to exit
                    event, values = window.read()
                    if event == sg.WIN_CLOSED or event == 'OK':
                        sys.exit(0)

            w = observe.weather
            window.close()
            wind = round(w.wind(unit='miles_hour')['speed'], 2) # I just want this value, not sure what the others are
            temp = round(w.temperature("fahrenheit")["temp"], 2) # Pull converted temp value from dict (not temp_min/max)
            layout = [ [sg.Text(f"Current weather for {values[0]}")], [sg.Text(f"Forecast: {w.detailed_status}")],
                       [sg.Text(f"Temperature: {temp}")], [sg.Text(f"Humidity: {w.humidity}%")],
                       [sg.Text(f"Wind speed: {wind} MPH")], [sg.Button('Exit')] ]
            window = sg.Window(welcome_str, layout)

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    break
        elif choice == 3:
            s_c()
            print(farewell)
            sys.exit(0)
    else:
        print_red(f"Input {choice.strip()} is invalid. Please enter an option number.")
        sleep(1)  # will give user time to read error before infinite menu loop repeats
