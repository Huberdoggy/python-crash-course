import re
import sys
from time import sleep

import PySimpleGUI as sg
from pyfiglet import Figlet
from termcolor import cprint

from cli_functions import add_to_path as atp
from cli_functions import build_request_url as build
from cli_functions import build_request_url_zip as build_z
from cli_functions import compile_patterns
from cli_functions import make_menu as mm
from cli_functions import make_request
from gui_functions import ask_city_or_zip as acz
from gui_functions import check_reg_city_state as check_cs
from gui_functions import check_reg_zip as check_zip
from gui_functions import determine_image
from gui_functions import draw_main_window as draw_main
from gui_functions import draw_zip_window as draw_z
from gui_functions import show_error_window as show_error
from gui_functions import weather_data_window as wdw
from open_weather_cli import choice_one

mod_paths = {
    "week6": "/home/huberdoggy/python-projects/python-crash-course/cyber245/week6",
}
atp(
    mod_paths
)  # insert my other modules in $PYTHONPATH.. using lst for room to expand if needed
from cars_and_trucks import format_main_menu as f_m
from cars_and_trucks import screen_clear as s_c

# Simple lambda functions to quickly convert print call color for 'x' argument provided
print_green = lambda x: cprint(x, "green")
print_red = lambda x: cprint(x, "red")

f = Figlet(font="standard")
welcome_str = "Kyle's Weather Retrieving App"
opts_lst = ["Run program from the CLI", "Run the GUI experience", "Quit"]
farewell = "Thank you for using the app. Good-bye!"
valid_int = False
reg_patterns = {
    "menu_sel_pattern": "^[1-3]{1}",
    "loc_pattern": "^[a-zA-Z]{2,}\s?([a-zA-Z]{2,})?$",
    "state_pattern": "^[a-zA-Z]{2}$",
    "zip_pattern": "^\d{5}",
}
raw_reg_dict = compile_patterns(
    reg_patterns
)  # I outsourced this to its own function to quickly compile all patterns in the list
# Make the main program menu by passing indexes of 'opts_lst' to my 'make_menu' function
options_dict = mm(opts_lst[0], opts_lst[1], opts_lst[2])

while not valid_int:
    f_m(welcome_str, options_dict)
    choice = input("=> ")
    if re.fullmatch(raw_reg_dict.get("menu_sel_pattern"), choice):
        valid_int = True
        choice = int(choice)  # After safely passing check, this can convert
        if choice == 1:
            s_c()
            still_running = choice_one()
            if still_running:
                valid_int = (
                    False  # repeat the menu selection loop from the top...
                )
        elif choice == 2:
            while True:
                first_win = acz()
                window = sg.Window("Pick One", first_win, size=(180, 100))
                event, values = window.read()
                if (
                    event == sg.WIN_CLOSED
                ):  # End program if user clicks the corner 'x'
                    sys.exit(0)
                elif event == "Search by Zip Code":
                    window.close()
                    # Create the next window
                    layout = draw_z()
                    window = sg.Window(welcome_str, layout)
                    event, values = window.read()
                    if event == "Exit" or event == sg.WIN_CLOSED:
                        sys.exit(0)  # Just end it
                    else:
                        zip = str(values[1]).strip()
                        result = check_zip(raw_reg_dict, zip)
                        if result:
                            full_url = build_z(zip)
                            my_dict = make_request(full_url)
                            window.close()
                            w_value = my_dict.get("description", "none")
                            im = determine_image(w_value)
                            weather_data = wdw(zip, my_dict, im)
                            print(weather_data)
                            window = sg.Window(welcome_str, weather_data)
                            event, values = window.read()
                            if event == "Exit" or event == sg.WIN_CLOSED:
                                sys.exit(0)
                            else:
                                window.close()
                                continue
                        else:
                            window.close()
                            show_error()
                else:
                    window.close()
                    layout = draw_main()
                    window = sg.Window(welcome_str, layout)
                    event, values = window.read()
                    if event == "Exit" or event == sg.WIN_CLOSED:
                        sys.exit(0)
                    else:
                        city, state = (
                            values[1],
                            values[2][:],
                        )  # Get first input and nested state abbrev
                        # Then, basically replicate everything from 'cli_functions' but manipulate the printing since
                        # I cant really call 'print_the_weather' the same way in the GUI
                        city, state = str(city).strip(), str(state).strip()
                        result = check_cs(raw_reg_dict, city, state)
                        if result:
                            full_url = build(city.title(), state.lower())
                            my_dict = make_request(full_url)
                            window.close()
                            w_value = my_dict.get("description", "none")
                            im = determine_image(w_value)
                            weather_data = wdw(city, my_dict, im)
                            print(weather_data)
                            window = sg.Window(welcome_str, weather_data)
                            event, values = window.read()
                            if event == "Exit" or event == sg.WIN_CLOSED:
                                sys.exit(0)
                            else:
                                window.close()
                                continue
                        else:
                            window.close()
                            show_error()
        elif choice == 3:
            s_c()
            print(farewell)
            sys.exit(0)
    else:
        print_red(
            f"Input {choice.strip()} is invalid. Please enter an option number."
        )
        sleep(
            1
        )  # will give user time to read error before infinite menu loop repeats
