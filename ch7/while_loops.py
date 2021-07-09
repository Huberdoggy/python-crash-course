# RENTAL CAR
# prompt = "What type of car would you like? => "
# choice = input(prompt)
# print(f"\nLet me se if I can find you a {choice.title()}.")

# RESTAURANT SEATING
# prompt = "How many people are in your dinner party? => "
# response = input(prompt)
# response = int(response)
#
# if response > 8:
#     print(f"I only have a table available for up to eight guests."
#           f"since you have {response} guests, you'll have to wait.")
# else:
#     print(f"I can fit {response} guests at a table over here. Follow me!")

# MULTIPLES OF TEN
#
# prompt = "Enter a number: => "
# number = int(input(prompt))
#
# if number % 10 == 0:
#     print(f"Your number {number} is a multiple of 10.")
# else:
#     print(f"Not a multiple of 10")

# PIZZA TOPPINGS

# prompt = "Enter a pizza topping."
# prompt += " Type 'quit' to stop at any time."
# choices = ""
# end_word = 'quit'
#
# while choices != end_word:
#     choices = input(prompt + " => ")
#     if choices != end_word:
#         print(f"Adding {choices} to your pizza")
#     else:
#         print("Thanks for your order. Exiting...")

# MOVIE TICKETS
# prompt = "Enter the age of the person in your party. Type 'quit' to stop. => "
# age = ""
# condition = True
#
# while condition:
#     age = input(prompt)
#     if age == 'quit':
#         condition = False
#         print("Exiting...")
#         break
#     else:
#         age = (int(age))
#         if age < 3:
#             print(f"This person is {age}, so their ticket is free.")
#         elif age >= 3 and age <= 12:
#             print(f"This person is {age}, so their ticket costs $10.")
#         elif age > 12:
#             print(f"This person is {age}, so their ticket costs $15.")

# DELI
# pastrami = 'pastrami'
# sandwich_orders = ['tuna', 'ham', 'tofu', 'steak', pastrami]
# finished_sandwiches = []
# flag = True
# word = 'quit'
# prompt = "Tell me what type of sammich to make you "
# prompt += "or enter 'quit' at anytime to leave => "
#
# while flag:
#     choice = input(f"\n{prompt}")
#     print('-' * 40)
#     if choice in sandwich_orders:
#         print(f"\nOkay..one second")
#         for sandwich in sorted(sandwich_orders):
#             if sandwich == choice:
#                 print(f"\n\tHere's the {choice.upper()} sandwich you requested.")
#                 finished_sandwiches.append(choice)
#             else:
#                 print(f"\n\tLots of leftover {sandwich} since nobody ordered a {sandwich.upper()} sandwich!")
#     elif choice == word:
#         print(f"You entered {choice}. Goodbye.")
#         flag = False
#     elif choice not in sandwich_orders:
#         print("I don't know how to make a " + choice + ' sandwich.')
#         flag = False
# print('-' * 40)
# if not finished_sandwiches:
#     print("The list is empty.")
# else:
#     print(f"\nHere's the completed sandwiches: ")
#     for sandwich in finished_sandwiches:
#         print(f"\n{sandwich.title()}")
#     print('-' * 40)
# # NO PASTRAMI
#     while pastrami in finished_sandwiches:
#         finished_sandwiches.remove(pastrami)
#     print(f"Removed all instances of pastrami: {finished_sandwiches}")

# DREAM VACATION
# responses = {}
#
# voting_active = True
#
# while voting_active:
#     name = input("What's your name? ")
#     response = input("What is your ideal dream vacation spot? ")
#
#     responses[name] = response
#     repeat = input("Would you like to let anybody else pipe in? ")
#     if repeat == 'no':
#         voting_active = False
# print("\n---VOTING RESULTS---")
# for name, response in sorted(responses.items()):
#     print(f"{name.title()} would like to travel to {response.title()}.")



