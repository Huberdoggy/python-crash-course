"""Write a program that uses a while loop to determine how long it takes for an investment to double
at a given interest rate. The input will be an annualized interest rate and the initial investment amount,
and the output is the number of years it takes an investment to double."""

import re, sys

# My regular expression will match user input to ensure strings combined with any whitespace
# or number sequence are NOT entered..
pattern = "^(\s+)?[a-zA-Z]{1,}(\s+)?[a-zA-Z0-9]{1,}(\s+)?$"

try:
    re.compile(pattern)
except re.error:
    print("Not a valid regex expression")


def get_simp_interest(P, R):
    # The formula to calc simple interest is - price * rate * time over 100
    si = (P * R) / 100
    return si


is_valid_input = False  # Don't flip this until valid input is registered for BOTH principal and interest

try:
    while not is_valid_input:
        principal = input("Please enter the initial investment amount => ")
        if re.fullmatch(pattern, principal):
            print(
                f"Your input '{principal.strip()}' is NOT a number. Please try again"
            )
        else:
            principal = float(principal)
            rate = input("Now, please enter the annual interest rate => ")
            if re.fullmatch(pattern, rate):
                print(
                    f"Your input '{rate.strip()}' is NOT a number. Please try again"
                )
            else:
                rate = float(rate)
                is_valid_input = True
except ValueError:
    print(
        f"The regex expression didn't detect the problem.\nEnsure your full input is numeric next time..good-bye"
    )
    sys.exit()


double_investment = principal * 2  # Determine what the double would be
year = 0  # initialize this variable to correspond to a 'count' of sorts, for the upcoming while loop
old_principal = (
    principal  # Store the original investment in its own variable for later...
)

while principal < double_investment:
    if year >= 1:
        print(f" - {year} year investment is: \t{round(principal, 2)}")
    new_interest = get_simp_interest(
        principal, rate
    )  # Continue to calc interest each iteration on the current P
    principal += new_interest  # Manipulate principal by adding the new interest each iteration
    if principal > double_investment:
        excessive_amt = round(principal - double_investment, 2)
    year += 1  # As stated above, this will ensure 'num of years' continues to track while the condition is True


gains = (
    principal - old_principal
)  # Store the difference from old to new as a variable
print(f"\n\t***THE VERDICT***\n")
# Finally, print the outcome formatted in a descriptive manner, rounding floats to 2 decimal places
print(
    f"In {year} years, the investment will be worth: {principal:.2f}, "
    f"which exceeds the double of your initial ${old_principal} investment by ${excessive_amt}\n"
    f"This is a total growth of ${gains:.2f}"
)
