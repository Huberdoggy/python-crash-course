# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Kyle Huber
# Creation Date: 09/07/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.
# You need to identify the issues and correct them.

import random
import time

# Added this function to consolidate some things at the bottom
def should_keep_playing(input_var):
    print("Do you want to play again? (yes or no)")
    get_new_input = input("=> ")
    if (
        get_new_input == input_var or get_new_input == "y"
    ):  # if they re-enter 'yes' or 'y'
        return True
    else:
        return  # will then exit the program as my variable for 'should_keep_playing' will check if False


def displayIntro():
    print(
        """\nYou are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight."""
    )
    print()


def chooseCave():
    cave = ""
    while (
        cave != "1" and cave != "2"
    ):  # Issue with indentation fixed to reflect PEP8 tab=4 spaces standard
        print("Which cave will you go into? (1 or 2)")
        cave = input()

    return cave  # fixed variable name to reflect the singular 'cave'


def checkCave(chosenCave):
    print("You approach the cave...")
    # sleep for 2 seconds
    time.sleep(2)
    print("It is dark and spooky...")
    # sleep for 2 seconds
    time.sleep(3)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    # sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print(
            "Gobbles you down in one bite!"
        )  # Fixed - added parentheses around print function


playAgain = "yes"
while True:  # Fixed - equality check needs to be double-equal for bool,
    # not assignment. Then, I modified this for my function to fix redundancy and simplify
    displayIntro()
    caveNumber = (
        chooseCave()
    )  # fixed - function name typo - need uppercase 'C' in chooseCave
    checkCave(caveNumber)

    check_again = should_keep_playing(playAgain)
    if not check_again:
        print("Thanks for playing")  # typo - fixed to 'playing'
        break
