import re
from termcolor import cprint
# Aliased function/s
from cli_functions import build_request_url as build, print_the_weather, \
    build_request_url_zip as build_z, make_request
# Simple lambda functions to quickly convert print call color for 'x' argument provided
print_red = lambda x: cprint(x, 'red')
reg_patterns = {
    'loc_pattern': '^[a-zA-Z]{2,}\s?([a-zA-Z]{2,})?$',
    'state_pattern': '^[a-zA-Z]{2}$',
    'zip_pattern': '^\d{5}',
}

def choice_one():
    while True:
        ask = input("Would you like to query by zip-code or city? (c/z)? => ")
        if ask == 'c':
            city = input("Enter the city name to check current forecast => ")
            state = input("Now, enter the 2 letter state code (ex. 'MN') => ")
            first_reg = reg_patterns.get('loc_pattern', 'empty')
            second_reg = reg_patterns.get('state_pattern', 'empty')
            if (re.fullmatch(first_reg, city.strip()) and re.fullmatch(second_reg, state.strip())):
                check_okay = input(f"You entered '{city.strip()}' and state code '{state.strip()}'. "
                                   f"Is this correct (y/n)? => ")
                if check_okay == 'y' or check_okay == 'Y':
                    city = city.title().strip()
                    state = state.lower().strip()
                    full_url = build(city, state)
                    my_dict = make_request(full_url)
                    print_the_weather(my_dict)
                    go_again = input("Would you like to make a new query? (y/n) => ")
                    if go_again == 'n' or go_again == 'N':
                        return True # pass this to 'menu_selection' so main menu commences
                    else:
                        continue
                else:
                    continue
            else:
                print_red("Invalid input. Ensure only letters are entered for city and state code.")
        elif ask == 'z':
            zip = input("Enter the five digit zip-code to query => ")
            strip_zip = zip.strip()  # To prevent potential error when sending request. Just like above
            if re.fullmatch(reg_patterns.get('zip_pattern'), strip_zip):  # Regex handles the rest
                check_okay = input(f"You entered '{strip_zip}'. Is this correct (y/n)? => ")
                if check_okay == 'y' or check_okay == 'Y':
                    full_url = build_z(strip_zip)
                    my_dict = make_request(full_url)
                    print_the_weather(my_dict)
                    go_again = input("Would you like to make a new query? (y/n) => ")
                    if go_again == 'n' or go_again == 'N':
                        return True # pass this to 'menu_selection' so main menu commences
                    else:
                        continue
                else:
                    continue
            else:
                print_red("Invalid zip code. Ensure you enter five digits with no space between.")
