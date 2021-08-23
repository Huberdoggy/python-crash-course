from os import system, name
from termcolor import cprint, colored
from pyfiglet import Figlet

print_green = lambda x: cprint(x, 'green') # Simple lambda to quickly convert
# print call color for 'x' argument provided
print_red = lambda x: cprint(x, 'red')

def screen_clear():
    # Function to accomplish the same thing as running term clear command to prevent clutter in prog
    if name == 'nt': # In the rarer circumstance I'm running on Windows
        _ = system('cls') # Store in underscore as variable to align with the fact a Py shell always stores
        # its last output in an underscore
    else: # For 'Nix
        _ = system('clear')


def format_main_menu(render_str, m_dict):
    f = Figlet(font='standard', justify='center')
    print(f"{colored(f.renderText(render_str), 'blue')}\n")
    print_green(f"\tPlease enter a number corresponding to one of the following:\n")
    print("\t" * 3 + ("*" * 30))
    for key in m_dict:
        print_green("\t" * 3 + str(key) + ' - ' + m_dict[key])
    print("\t" * 3 + ("*" * 30))


def get_vehicle_attribs(vehicle):
    vehicle_obj = [vehicle.getMake().title(), vehicle.getModel().title(),
               vehicle.getColor(), vehicle.getFuelType()]
    return vehicle_obj
    # This was they only way I could get it to not print the literal class object
    # I was going to use __str__ overrides in constructor but wasn't quite sure howto work it in


#### CLASSES ####

# Parent constructor. Options are common to all vehicles and the user must choose at least 1 regardless of car/truck
class Vehicle:

    def __init__(self, fuelType='premium octane gas'):
        self.make = input("Enter the make => ")
        self.model = input("Enter the model => ")
        self.color = input("Enter the color => ")
        self.fuelType = fuelType
        self.options = ['Power Mirrors', 'Power Steering', 'Cruise Control', 'Remote Start'
                        'Backup Camera', 'Bluetooth', 'Anti-Lock Brakes', 'Heated Mirrors']


    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuelType

    def getOptions(self):
        pass