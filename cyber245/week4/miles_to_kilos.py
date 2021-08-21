import re, sys
from termcolor import cprint
sys.path.insert(1, '/home/huberdoggy/python-projects/python-crash-course/cyber245/week9')
# print('\n'.join(sys.path)) # I was messing with importing modules from custom dirs, so I had to do some
# __init__ magic in Pycharm and I wanted to see what sys.path was doing
from cli_functions import compile_patterns as c_p # From my sister directory for the OpenWeather functions
from prog_funcs import conv_to_kilos
print_red = lambda x: cprint(x, 'red') # Simple lambda to quickly convert print call color for 'x' argument provided
error_msg = """Your input is invalid.
Ensure you enter numbers only.
Float values are optional (i.e '100' or '100.25) and must not exceed 2 decimal places."""
beginning_sub = error_msg[:10] # Going to play with something new for this program - substring concat

reg_patterns = {
    'input_miles': '^\d{1,5}\.?(\d{1,2})?$', # If they use a decimal number, I don't think accepting more than 2
    # decimal places in the input is necessary
}

c_p(reg_patterns) # Compile the reg expressions..only 1 right now but makes it easy for mass use

go_again = True # set up the infinite loop

while go_again:
    num_miles = input("Please enter the total number of miles you've driven (or 'q' to quit) => ")
    if num_miles == 'q':
        break
    elif not re.fullmatch(reg_patterns.get('input_miles', 'empty'), num_miles):
        print_red(beginning_sub + ' ' + num_miles.strip() + error_msg[10:])
    else:
        num_miles = float(num_miles)
        conv_to_kilos(num_miles)
        ask = input("Make another query (y/n)? => ")
        if ask == 'n':
            go_again = False # End the loop
            print("Until next time then. Good-bye!")







