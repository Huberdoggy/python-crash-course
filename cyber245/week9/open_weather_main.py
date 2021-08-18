# Terminal colors, fun fonts, and essential modules for API calls
import requests, re, sys, json
from pyfiglet import Figlet
from termcolor import colored, cprint
# Aliased function/s
from cli_functions import make_menu as mm, build_request_url as build, print_the_weather

# Simple lambda functions to quickly convert print call color for 'x' argument provided
print_green = lambda x: cprint(x, 'green')
print_red = lambda x: cprint(x, 'red')

f = Figlet(font='standard')
welcome_str = "Kyle\'s Weather Retrieving App"
opts_lst = ['Run program from the CLI', 'Run the GUI experience', 'Quit']
menu_sel_pattern = "^[1-3]{1}$"
farewell = "Thank you for using the app. Good-bye!"

try:
    re.compile(menu_sel_pattern)
except re.error:
    print("Not a valid regex pattern.")

# Make the main program menu by passing indexes of 'opts_lst' to my 'make_menu' function
options_dict = mm(opts_lst[0], opts_lst[1], opts_lst[2])

print(f"{colored(f.renderText(welcome_str), 'red')}\n")
print_green(f"Please enter a number corresponding to one of the following:\n")
print("\t" + ("*" * 30))
for key in options_dict:
    print_green(f"\t{key} - {options_dict[key]}")
print("\t" + ("*" * 30))
try:
    while True:
        choice = input("=> ")
        if not re.fullmatch(menu_sel_pattern, choice):
            print_red(f"Input {choice.strip()} is invalid. Please enter an option number.")
        else:
            choice = int(choice) # After safely passing check, this can convert
            if choice == 1:
                check_bool = False
                while not check_bool:
                    city = input("Enter the city name to check current forecast => ")
                    state = input("Now, enter the 2 letter state code (ex. 'MN') => ")
                    check_okay = input(f"You entered '{city}' and state code '{state}'. Is this correct (y/n)? => ")
                    if check_okay == 'y' or check_okay == 'Y':
                        city = city.title()
                        state = state.lower()
                        check_bool = True
                        full_url = build(city, state)
                        try:
                            response = requests.get(full_url)
                            j_response = response.json() # 'response' now holds a lst of nested dictionaries
                        # from the endpoint. We will check if the 'cod' key equals 404 - the web request status code
                        # for 'resource not found'
                            if ["cod"] != "404":
                                nested_1 = j_response["main"] # Here, 'main' is an object of interest to me
                                # returned by the request -> it's a nested dict
                                # which holds useful data...in particular 'temperatures'
                                current_temp = nested_1["temp"]
                                current_pressure = nested_1["pressure"]
                                current_humidity = nested_1["humidity"]
                                # Now, traverse up to the 'weather' info
                                w = j_response["weather"]
                                # 'Weather description is located at [weather][0]
                                weather_desc = w[0]["description"]
                                print_the_weather(current_temp, current_pressure, current_humidity, weather_desc)
                                go_again = input("Would you like to make a new query? (y/n) => ")
                                if go_again == 'n' or go_again == 'N':
                                    print(farewell)
                                    sys.exit()
                                else:
                                    check_bool = False # Go back to city/state input
                            else:
                                print(f"Data for {city} not found.")
                        except requests.exceptions.RequestException as e:
                            raise sys.exit(e) # Make 'e' correspond to the error code. Hopefully catch any extraneous
                    # else: # Ask for city again to verify spelling
                    #     continue ... not needed now that bool is never flipped to 'True'
            elif choice == 2:
                pass
            elif choice == 3:
                print(farewell)
                break
except ValueError: # Fail safe..
    print("Failed to register. Please ensure you enter one of the numeric options.")
    sys.exit(1)

