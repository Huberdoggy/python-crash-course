import re
from termcolor import cprint

def compile_patterns(pattern_dict):
    for value in pattern_dict.values():
        try:
            re.compile(value)
            return pattern_dict
        except re.error:
            print(f"Invalid regex expression {value}")

def conv_to_kilos(miles):
    kilos = miles * 1.609344
    print_green(f"\n\t***CONVERSION RESULT***\n")
    print('\t' + '-' * 40)
    print(f"\tYour distance driven in miles: {miles}\n"
          f"\tEquivalent number of kilometers: {kilos:.3f}")
    print('\t' + '-' * 40)
    return kilos

# Simple lambda functions to quickly convert print call color for 'x' argument provided
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
# error_prefix = "Your input invalid"
error_msg = """Your input is invalid.
Ensure you enter numbers only.
Float values are optional (i.e '100' or '100.25) and must not exceed 2 decimal places."""
beginning_sub = error_msg[:10] # Going to play with something new for this program - substring concat

reg_patterns = {
    'input_miles': '^\d{1,5}\.?(\d{1,2})?$', # If they use a decimal number, I don't think precision for more than 2
    # places is necessary
}

compile_patterns(reg_patterns) # Compile the reg expressions..only 1 right now but makes it easy for mass use

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
            go_again = False
            print("Until next time then. Good-bye!")







