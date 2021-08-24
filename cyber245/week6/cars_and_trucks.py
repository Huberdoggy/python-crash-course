import re
from os import system, name
from termcolor import cprint, colored
from pyfiglet import Figlet

print_green = lambda x: cprint(x, 'green') # Simple lambda to quickly convert
# print call color for 'x' argument provided
print_red = lambda x: cprint(x, 'red')

pattern = "^.[a-z]{4}.[a-z]{3}.[a-z]{6}\.Car.*" # for matching whether 'Car' or 'Truck' obj is passed to get_attribs func
pattern2 = "^[a-zA-Z].*$"
try:
    re.compile(pattern)
    re.compile(pattern2)
except re.error:
    print("Invalid regex expression")

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

def show_garage(vehicle_lst):
    if len(vehicle_lst) > 0:
        print_green(f"\n\t*** CURRENT GARAGE ***\n")
        for k, v in vehicle_lst.items():
            print(f"{k} -> {str(v)}\n")
    else:
        print_red("The garage is currently empty.")


def get_vehicle_attribs(vehicle):
    # print(vehicle)
    if re.fullmatch(pattern, str(vehicle)):
        vehicle_obj = [vehicle.make.title(), vehicle.model.title(),
               vehicle.color, vehicle.fuelType, vehicle.engineSize, vehicle.numDoors, vehicle.options]
    else:
        vehicle_obj = [vehicle.make.title(), vehicle.model.title(),
                       vehicle.color, vehicle.fuelType, vehicle.cabStyle, vehicle.bedLength, vehicle.options]
    return vehicle_obj
    # This was they only way I could get it to not print the literal class object
    # I was going to use __str__ overrides in constructor but wasn't quite sure howto work it in


#### CLASSES ####

# Parent constructor. Options are common to all vehicles and the user must choose at least 1 regardless of car/truck
class Vehicle:

    def __init__(self, engineSize=None, numDoors=None, cabStyle=None, bedLength=None):
        # These will be overridden by child classes
        self.engineSize = engineSize
        self.numDoors = numDoors
        self.cabStyle = cabStyle
        self.bedLength = bedLength
        self.options = ['Power Mirrors', 'Power Steering', 'Cruise Control', 'Remote Start',
                        'Backup Camera', 'Bluetooth', 'Anti-Lock Brakes', 'Heated Mirrors']


    def build_opts_menu(self): # First, I'm going to build a dict of opts, similar to main-menu
        my_dict = {}
        count = 1
        for option in self.options:
            my_dict[count] = option
            count += 1
        self.options = my_dict
        return my_dict


    def getMake(self):
        self.make = input("Enter the make => ")
        return self.make

    def getModel(self):
        self.model = input("Enter the model => ")
        return self.model

    def getColor(self):
        self.color = input("Enter the color => ")
        return self.color

    def getFuelType(self):
        f_type = input("E-85 or gas (e/g)? => ")
        if f_type == 'g':
            self.fuelType = 'premium octane gas'
        else:
            self.fuelType = 'E-85'
        return self.fuelType

    def getOptions(self, render_str, m_dict): # Now I'm passing the dictionary to my 'cool formatting' func
        screen_clear()
        f = Figlet(font='standard', justify='center')
        print(f"{colored(f.renderText(render_str), 'blue')}\n")
        print_green(f"\tPlease enter numbers corresponding to the following options\n"
                    f"\tto add to the vehicle. You must choose 1 at minimum:\n")
        print("\t" * 3 + ("*" * 30))
        for key in m_dict:
            print_green("\t" * 3 + str(key) + ' - ' + m_dict[key])
        print("\t" * 3 + ("*" * 30))
        chosen_opt_lst = []
        my_flag = True
        try:
            # my_flag = True
            while my_flag:
                num_choice = input("Enter a number to add that option to your vehicle (or 'q' to return) => ")
                if re.fullmatch(pattern2, num_choice.strip()):
                    if num_choice == 'q' and len(chosen_opt_lst) < 1:
                        print_red("You must add at least 1 option.")
                    elif num_choice == 'q' and len(chosen_opt_lst) >= 1:
                        screen_clear()
                        return chosen_opt_lst
                    else:
                        print_red(f"Input {num_choice.strip()} is not an option.")
                elif not re.fullmatch(pattern2, num_choice):
                    num_choice = int(num_choice)
                    if num_choice in range(1, 9):
                        num_choice = m_dict[num_choice]
                        chosen_opt_lst.append(num_choice)
                        print("[+] Added " + colored(num_choice, 'green') + " to your vehicle.")
                        if len(chosen_opt_lst) >= 1:
                            add_more = input("Add more? (y/n)? => ")
                            if add_more == 'n':
                                screen_clear()
                                return chosen_opt_lst
                    else:
                        print_red(f"{num_choice} is an invalid choice.")
        except ValueError:
            print("I don't understand that option")
            return


class Car(Vehicle):
    """ The assignment is worded sort of confusing but essentially, I'm not going to use the parent class
    for anything other than options and functions for this 'input' to inherit correctly"""
    def __init__(self):
        super().__init__()
        self.make = Car.getMake(self)
        self.model = Car.getModel(self)
        self.color = Car.getColor(self)
        self.fuelType = Car.getFuelType(self)
        self.engineSize = Car.getEngineSize(self)
        self.numDoors = Car.getNumDoors(self)
        car_opts_dict = Car.build_opts_menu(self)
        self.options = Car.getOptions(self, 'Vehicle Options', car_opts_dict)

    def getEngineSize(self):
        e_size = int(input("Drive a V6 or V8 (6/8)? => "))
        if e_size == 6:
            self.engineSize = 'V6'
        else:
            self.engineSize = 'V8'
        return self.engineSize

    def getNumDoors(self):
        num_doors = int(input("2 or 4 doors (2/4)? => "))
        if num_doors == 4:
            self.numDoors = "four doors"
        else:
            self.numDoors = "two doors"
        return self.numDoors



class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.make = Truck.getMake(self)
        self.model = Truck.getModel(self)
        self.color = Truck.getColor(self)
        self.fuelType = Truck.getFuelType(self)
        self.cabStyle = Truck.getCabStyle(self)
        self.bedLength = Truck.getBedLength(self)
        truck_opts_dict = Truck.build_opts_menu(self)
        self.options = Truck.getOptions(self, 'Vehicle Options', truck_opts_dict)

    def getCabStyle(self):
        c_style = input("Crew cab or extended (c/e)? => ")
        if c_style == 'c':
            self.cabStyle = 'crew cab'
        else:
            self.cabStyle = 'extended cab'
        return self.cabStyle


    def getBedLength(self):
        b_length = input("Standard bed or long bed (s/l)? => ")
        if b_length == 's':
            self.bedLength = 'standard bed'
        else:
            self.bedLength = 'long bed'
        return self.bedLength


