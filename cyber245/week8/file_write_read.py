import re, sys
from time import sleep
from termcolor import colored
from file_funcs import add_to_path as atp, expand_env_vars as exp_vars, \
    does_fpath_exist as does_exist, store_data
mod_paths = ['/home/huberdoggy/python-projects/python-crash-course/cyber245/week9',
                             '/home/huberdoggy/python-projects/python-crash-course/cyber245/week6']
atp(mod_paths) # Quickly insert addl paths into $PYTHONPATH for my other module dirs
from cli_functions import compile_patterns as c_p
from cars_and_trucks import screen_clear as s_c
reg_patterns = {
    'filename_input': '^[a-zA-Z]{1,}(_|\-)?(\d{1,})?(\w{1,})?$',
    'name': '^[a-zA-Z]{2,}$',
    'address': '^[0-9]{1,}\s[a-zA-Z0-9]{1,15}\s[a-zA-Z]{1,15}\s?(\w{1,5})?$', # this should cover enough
    # --> house number, space, street num with suffix, space, street name,
    # optional - space and cardinal direction
    'phone_num': '^\d{3}\d{3}\d{4}$', # for user convenience, I wont require hyphens or literal parentheses
}

user_info = {}

c_p(reg_patterns)
prog_file_path = exp_vars() # Expand $HOME on Linux
s_c()
full_file_path = does_exist(prog_file_path, reg_patterns) # will return True if my base-path variable exists and
# build filename + suffix from user input
name_valid, address_valid, phone_valid = False, False, False

while not name_valid:
    get_name = input("Now, what's your name? => ")
    if re.fullmatch(reg_patterns.get('name', 'empty'), get_name.strip()):
        user_info['Name'] = get_name.strip()
        name_valid = True
    else:
        print(colored(f"{get_name.strip()} is not the correct format for 'name'.", 'red'))
        continue
    while not address_valid:
        get_addy = input("Now, whats your address (space separated)? => ")
        if re.fullmatch(reg_patterns.get('address', 'empty'), get_addy.strip()):
            user_info['Address'] = get_addy.strip()
            address_valid = True
        else:
            print(colored(f"{get_addy.strip()} is not the correct format for 'address'.", 'red'))
            continue
        while not phone_valid:
            get_phone = input("Please enter your phone number.\nFor your convenience, I require digits only => ")
            if re.fullmatch(reg_patterns.get('phone_num', 'empty'), get_phone.strip()):
                user_info['Phone'] = get_phone.strip()
                phone_valid = True
            else:
                print(colored(f"{get_phone.strip()} is not the correct format for 'phone'.", 'red'))

s_c()
should_write = input("Should I write this data to file? (y/n) => ")
if should_write == 'n':
    print("Discarded. Good-bye!")
    sys.exit(0)
else:
    dump_display_data = store_data(full_file_path, user_info)
    print("Now retrieving written data from the file....")
    sleep(3)
    s_c()
    print(dump_display_data)






