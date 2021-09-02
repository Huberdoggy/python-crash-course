import re, sys
from time import sleep
import PySimpleGUI as sg
from pyfiglet import Figlet
from termcolor import cprint
from open_weather_cli import choice_one
from cli_functions import build_request_url as build, make_request

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
            # layout = [[sg.Text('Enter the city name'), sg.InputText()],
            #           [sg.Text('Enter the state code'), sg.InputText()],
            #           [sg.Button("Search Location"), sg.Button("Exit")]]  # Create the window
            # window = sg.Window(welcome_str, layout)
            # Create an event loop
            while True:
                layout = [[sg.Text('Enter the city name'), sg.InputText()],
                          [sg.Text('Enter the state code'), sg.InputText()],
                          [sg.Button("Search Location"), sg.Button("Exit")]]  # Create the window
                window = sg.Window(welcome_str, layout)
                event, values = window.read()
                # End program if user closes window or
                # presses the Exit button
                if event == "Exit" or event == sg.WIN_CLOSED:
                    sys.exit(0)  # Just end it
                else:
                    city, state = values[0], values[1][:] # Get first input and nested state abbrev
                    # Then, basically replicate everything from 'cli_functions' but manipulate the printing since
                    # I cant really call 'print_the_weather' the same way in the GUI
                    full_url = build(str(city).title().strip(), str(state).lower().strip())
                    my_dict = make_request(full_url)
                    window.close()
                    layout = [ [sg.Text(f"Current weather for {str(city).title().strip()}")],
                       [sg.Text(f"Temperature in Fahrenheit: {str(my_dict['temp'])}")],
                       [sg.Text(f"Atmospheric pressure (in psi): {my_dict['pressure']:.1f}")],
                       [sg.Text(f"Humidity: {str(my_dict['humidity'])}%")],
                       [sg.Text(f"Forecast is showing: {str(my_dict['description'])}")],
                       [sg.Button('New Query')], [sg.Button('Exit')] ]
                    window = sg.Window(welcome_str, layout)
                    event, values = window.read()
                    if event == 'Exit' or event == sg.WIN_CLOSED:
                        sys.exit(0)
                    else:
                        window.close()
                        continue
        elif choice == 3:
            s_c()
            print(farewell)
            sys.exit(0)
    else:
        print_red(f"Input {choice.strip()} is invalid. Please enter an option number.")
        sleep(1)  # will give user time to read error before infinite menu loop repeats
