import random
import sys
from random import randint, choice


# DICE
# class Die:
#
#     def __init__(self, name, sides=6):
#         self.name = name
#         self.sides = sides
#
#     def roll_die(self):
#         sides = random.randint(1, self.sides)
#         count = 1
#         print("-" * 20)
#         print(f"Rolling {self.name}")
#         print("-" * 20)
#         for i in range(1, 11):
#             print(f"Roll count: {count}\nValue: {sides}")
#             sides = random.randint(1, self.sides)
#             count += 1
#
#
# my_die = Die('Die 1', 10)
# my_die2 = Die('Die 2', 20)
# my_die.roll_die()
# my_die2.roll_die()

# LOTTERY


def lucky_day(my_ticket):
    win = False
    count = 1
    all_values = (
        5005,
        200,
        "A",
        30.5,
        15025,
        "K",
        "z",
        42,
        7020,
        "g",
        "H",
        14,
        29,
        855,
        56,
    )
    winning_values = []
    while not win:
        for i in range(1, 5):
            selected_winner = choice(all_values)
            winning_values.append(selected_winner)
        if my_ticket == winning_values:
            win = True
            print("\n")
            string = f"Congrats Kyle, you won the lottery!!!"
            print(string.upper())
            print(f"Total number of rounds it took to get a win: {count}")
            print(f"\n\t****LOTTERY OUTCOME****")
            print(f"Winning values are: {winning_values}")
            print(f"Kyle's picks are: {my_ticket}")
        else:
            print(f"Currently on attempt: {count} with no win")
            winning_values = []
            count += 1


ticket = ["K", 200, "H", 42]
lucky_day(ticket)
