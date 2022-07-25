import re, sys
from termcolor import cprint, colored

sys.path.insert(
    1, "/home/huberdoggy/python-projects/python-crash-course/cyber245/week9"
)  # for my previous functions
from cli_functions import compile_patterns as c_p
from prog_funcs import make_ticker_dict as m_d
from prog_funcs import get_extended_ticker_data as get_ex

print_red = lambda x: cprint(
    x, "red"
)  # Simple lambda to quickly convert print call color for 'x' argument provided

reg_patterns = {"ticker_input": "^[a-zA-Z]{2,5}$"}

ticker_list = [
    "aapl",
    "msft",
    "googl",
    "amzn",
    "fb",
    "tsla",
    "nvda",
    "jpm",
    "wmt",
    "unh",
]  # list of ticker strings to be passed to function. Will return dict of keys with real-time values

c_p(
    reg_patterns
)  # Compile the reg expressions..only 1 right now but makes it easy for mass use

ticker_dict = m_d(ticker_list)
# for key in ticker_dict:
#     print(f"\n{key}: {ticker_dict[key]}")

or_quit = "Or press 'q' to quit"
not_in_dict = "No quote for abbreviation"  # substring for 'else' block

ticker_quote = True

while ticker_quote:
    choose_ticker = input(
        f"\nPlease enter the desired ticker to retrieve current price {or_quit} => "
    )
    if choose_ticker == "q":
        break
    elif not re.fullmatch(
        reg_patterns.get("ticker_input", "empty"), choose_ticker
    ):
        print_red(
            f"Your input {choose_ticker.strip()} is not in the correct format."
            f"\nEnsure 2-5 letters only\nWith no space in between."
        )
    else:
        choose_ticker = (
            choose_ticker.strip().lower()
        )  # ensure surrounding white space is removed and input matches
        # dict case
        if choose_ticker in ticker_dict:
            color_ticker = colored(
                choose_ticker.upper(), "green"
            )  # format substring in color for easy sighting
            print(
                f"\nAccording to Yahoo Finance, the current price for '{color_ticker}' is: "
                f"${ticker_dict[choose_ticker]:.3f}"
            )
            stock_table = get_ex(choose_ticker)
            print(
                colored(
                    f"\n\t\t*** DATA FROM THE PAST WEEK FOR {choose_ticker.upper()} ***",
                    "green",
                )
            )
            print(f"\n{stock_table}")
            go_again = input(
                f"\nWould you like to make another query? (y/n) => "
            )
            if go_again == "n":
                ticker_quote = False
                print("Until next time then. Good-bye!")
        else:
            print_red(f"{not_in_dict} '{choose_ticker.upper()}' found.")
