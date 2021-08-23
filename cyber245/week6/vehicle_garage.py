import sys
from termcolor import cprint, colored
from time import sleep
from cars_and_trucks import screen_clear as s_c, format_main_menu as fmm, get_vehicle_attribs as get_attribs, Vehicle
sys.path.insert(1, '/home/huberdoggy/python-projects/python-crash-course/cyber245/week9') # for my previous functions
from cli_functions import make_menu as mm

# Define various variables for fast color prints and strs
print_red = lambda x: cprint(x, 'red') # Simple lambda to quickly convert print call color for 'x' argument provided
print_green = lambda x: cprint(x, 'green')
opts_lst = ['Build a Car', 'Build a Pickup Truck', 'Quit'] # To pass to 'mm' as main menu opts
welcome_str = "Kyle\'s Virtual Garage"
farewell = "Thank you for using the app. Good-bye!"
vehicle_garage = {} # Will hold completed vehicles as key/vals

#Build main menu
main_menu_dict = mm(opts_lst[0], opts_lst[1], opts_lst[2])
fmm(welcome_str, main_menu_dict) # build and format w/ Figlet
try:
    show_menu = True
    while show_menu:
        num_choice = int(input("=> "))
        if num_choice in range(1, 3):
            if num_choice == 1: # For car creation
                show_menu = False
                color_choice = colored('Car', 'green')
                print(f"You will now be directed to {color_choice} specific questions...")
                sleep(3)
                s_c()
                check_done = False
                car_count = 1
                while not check_done:
                    new_car = Vehicle()
                    vroom = input(f"Your new {new_car.getMake().title()}, {new_car.getModel().title()} "
                      f"is {new_car.getColor()} and runs on {new_car.getFuelType()}."
                      f" Add this this car to the garage (y/n)? => ")
                    if vroom == 'y':
                        add_car = get_attribs(new_car)
                        vehicle_garage[f'Vehicle {str(car_count)}'] = add_car
                        print_green(f"\n\t*** CURRENT GARAGE ***\n")
                        for k,v in vehicle_garage.items():
                            print(f"{k} -> {str(v)}\n")
                        add_another = input("Add more cars? (y/n) => ")
                        if add_another == 'y':
                            car_count += 1
                        else:
                            check_done = True
                            s_c()
                            fmm(welcome_str, main_menu_dict)
                            show_menu = True # Run from the top
                    else:
                        print(f"Discarded the {new_car.getModel().title()}.")
            else: # For truck creation
                color_choice = colored('Truck', 'green')
                print(f"You will now be directed to {color_choice} specific questions...")
                sleep(3)
                s_c()
        elif num_choice == 3:
            sys.exit(0)
        else:
            print_red(f"Your selection {num_choice} is invalid.")
except ValueError: # for strings or anything else
    print_red(f"Failed to register.")
    sys.exit(1)