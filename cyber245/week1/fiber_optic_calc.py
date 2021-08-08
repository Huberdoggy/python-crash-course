"""Create a flowchart and write pseudocode for the following steps:
Display a welcome message for your program.
Get the company name from the user.
Get the number of feet of fiber optic to be installed from the user.
Multiply the total cost as the number of feet times $0.87.
Display the calculated information and company name. """

def calcTotal(number):
    # Multiply the total number of feet by 0.87
    number *= 0.87
    return number


prog_name = "kyle's fiber-optic cable price calculator"
message = print(f"\t***{prog_name.upper()}***")

while True: # Run the program until they choose to end it
    comp_name = input("Please enter the name of your company (or press 'q' to quit) => ") # get their company name
    if comp_name == 'q':
        break
    else:
        try:
            num_of_feet = int(input("Now, please enter the required amount of fiber cable to be installed"
                    " (i.e, the number in feet) => ")) # store number of feet as a variable
            total_calc = calcTotal(num_of_feet) # pass the previous variable to my calculation function
            print(f"Thank you!\nAccording to my calculations, {comp_name.title()} will require: ${total_calc} dollars"
      f" to accommodate {num_of_feet} feet of fiber optic cable.") # format the end result
        except ValueError:
            print(" Please enter a integer WHOLE number...")

