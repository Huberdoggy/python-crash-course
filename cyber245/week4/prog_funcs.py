from termcolor import colored

def conv_to_kilos(miles):
    kilos = miles * 1.609344 # Conversion factor of 1.6xx kilos for every mile
    print(colored(f"\n\t\t***CONVERSION RESULT***\n", 'green'))
    print('\t' + '-' * 40)
    print(f"\tYour distance driven in miles: {miles}\n"
          f"\tEquivalent number of kilometers: {kilos:.3f}")
    print('\t' + '-' * 40)
    return kilos