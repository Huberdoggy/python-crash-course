""" PART 1
Create a flowchart and write pseudocode for the following steps:
Display a welcome message for your program.
Get the company name from the user.
Get the number of feet of fiber optic to be installed from the user.
Multiply the total cost as the number of feet times $0.87.
Display the calculated information and company name.

PART 2
Now, you will implement “if statements” in a program by modifying the program you created in Part 1.
In Part 1, you calculated the total cost of fiber cable installation by multiplying the number of feet by $0.87.
Now you will evaluate a bulk discount. Modify your Part 1 program so that if users purchase more than 100 feet,
they are charged $0.80 per foot. If the user purchases more than 250 feet they will be charged $0.70 per foot.
If they purchase more than 500 feet they will be charged $0.50 per foot.
"""

import re

# My regular expression will match user input of at least 2 digits followed by a literal '.' and 2 or more digits
pattern = "\d{2,}\.\d{2,}"

try:
    re.compile(pattern)
    # print("Valid regex pattern")
except re.error:
    print("Non valid regex pattern.")


def calcTotal(number):
    # If number is greater than 100, apply discount appropriately
    if number > 100 and number <= 250:
        number *= 0.80
    # If number is greater than 250, apply discount appropriately
    elif number > 250 and number <= 500:
        number *= 0.70
    # If number is greater than 500, apply discount appropriately
    elif number > 500:
        number *= 0.50
    else:
        # Multiply the total number of feet by 0.87
        number *= 0.87
    return number


prog_name = "kyle's fiber-optic cable price calculator"
message = print(f"\t***{prog_name.upper()}***")

while True:  # Run the program until they choose to end it
    comp_name = input(
        "Please enter the name of your company (or press 'q' to quit) => "
    )  # get their company name
    if comp_name == "q":
        break
    else:
        try:
            num_of_feet = input(
                "Now, please enter the required amount of fiber cable to be installed"
                " (i.e, the number in feet) => "
            )  # store number of feet as a variable
            if re.fullmatch(pattern, num_of_feet):
                num_of_feet = float(num_of_feet)
            else:
                num_of_feet = int(num_of_feet)
            total_calc = calcTotal(
                num_of_feet
            )  # Pass the pre-determined float or int to my calculation function
            # Print a formatted result rounded to 2 decimal places
            print(
                f"Thank you!\nAccording to my calculations, {comp_name.title()} will require:"
                f" ${total_calc:.2f} dollars to accommodate {num_of_feet} feet of fiber optic cable."
            )
        except ValueError:
            print("Check you input, something else is going on...")
