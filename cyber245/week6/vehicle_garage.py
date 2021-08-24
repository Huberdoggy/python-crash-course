import sys
from termcolor import cprint, colored
from time import sleep
from cars_and_trucks import screen_clear as s_c, format_main_menu as fmm, show_garage, \
get_vehicle_attribs as get_attribs, Car, Truck
sys.path.insert(1, '/home/huberdoggy/python-projects/python-crash-course/cyber245/week9') # for my previous functions
from cli_functions import make_menu as mm

# Define various variables for fast color prints and strs
print_red = lambda x: cprint(x, 'red') # Simple lambda to quickly convert print call color for 'x' argument provided
print_green = lambda x: cprint(x, 'green')
opts_lst = ['Build a Car', 'Build a Pickup Truck', 'Show Garage', 'Quit'] # To pass to 'mm' as main menu opts
welcome_str = "Kyle\'s Virtual Garage"
farewell = "Thank you for using the app. Good-bye!"
vehicle_garage = {} # Will hold completed vehicles as key/vals
car_count = 0 # global so that if user re-enters after backing out to main menu, the count still holds
truck_count = 0

#Build main menu
main_menu_dict = mm(opts_lst[0], opts_lst[1], opts_lst[2], opts_lst[3])
fmm(welcome_str, main_menu_dict) # build and format w/ Figlet
try:
    show_menu = True
    while show_menu:
        num_choice = int(input("=> "))
        if num_choice in range(1, 5):
            if num_choice == 1: # For car creation
                show_menu = False
                color_choice = colored('Car', 'green')
                print(f"You will now be directed to {color_choice} specific questions...")
                sleep(3)
                s_c()
                check_done = False
                while not check_done:
                    new_car = Car()
                    vroom = input(f"Your new {new_car.make.title()} {new_car.model.title()} "
                      f"is {new_car.color} and runs on {new_car.fuelType}.\nIt has a {new_car.engineSize} engine"
                                  f" and {new_car.numDoors} doors.\n"
                                  f"Your options: {new_car.options}\nAdd this car to the garage (y/n)? => ")
                    if vroom == 'y':
                        car_count += 1
                        add_car = get_attribs(new_car)
                        vehicle_garage[f'Car {str(car_count)}'] = add_car
                        print_green(f"\n\t*** CURRENT GARAGE ***\n")
                        for k,v in vehicle_garage.items():
                            print(f"{k} -> {str(v)}\n")
                        add_another = input("Add more cars? (y/n) => ")
                        if add_another == 'n':
                            check_done = True
                            s_c()
                            fmm(welcome_str, main_menu_dict)
                            show_menu = True # Run from the top
                    elif vroom == 'n' and car_count < 1:
                        print_red(f"Discarded the {new_car.model.title()}. But, you must add at least 1"
                              f" car to the garage.")
                    else:
                        print_red(f"Discarded the {new_car.model.title()}.")
            elif num_choice == 2: # For truck creation
                color_choice = colored('Truck', 'green')
                print(f"You will now be directed to {color_choice} specific questions...")
                sleep(3)
                s_c()
                check_done = False
                while not check_done:
                    new_truck = Truck()
                    vroom = input(f"\nYour new {new_truck.make.title()} {new_truck.model.title()} "
                                  f"is {new_truck.color} and runs on {new_truck.fuelType}.\n"
                                  f"It has a {new_truck.cabStyle} and a {new_truck.bedLength}.\n"
                                  f"Your options: {new_truck.options}\nAdd this truck to the garage (y/n)? => ")
                    if vroom == 'y':
                        truck_count += 1
                        add_truck = get_attribs(new_truck)
                        vehicle_garage[f'Truck {str(truck_count)}'] = add_truck
                        print_green(f"\n\t*** CURRENT GARAGE ***\n")
                        for k,v in vehicle_garage.items():
                            print(f"{k} -> {str(v)}\n")
                        add_another = input("Add more trucks? (y/n) => ")
                        if add_another == 'n':
                            check_done = True
                            s_c()
                            fmm(welcome_str, main_menu_dict)
                            show_menu = True # Run from the top
                    elif vroom == 'n' and truck_count < 1:
                        print_red(f"Discarded the {new_truck.model.title()}. But, you must add at least 1"
                              f" truck to the garage.")
                    else:
                        print_red(f"Discarded the {new_truck.model.title()}.")
            elif num_choice == 3:
                show_garage(vehicle_garage)
            elif num_choice == 4:
                sys.exit(0)
        else:
            print_red(f"Your selection {num_choice} is invalid.")
except ValueError: # for strings or anything else
    print_red(f"Failed to register.")
    sys.exit(1)