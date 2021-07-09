# my_cars = ['camaro', 'Audi', 'corvette', 'bmw']
# for car in my_cars:
#     if car == 'camaro':
#         print(f"My first sports car was a {car.upper()}")
#     else:
#         print(car.title())

# age = 20
# age2 = 25
# # print(f"Is {age} >= 21? I predict True")
# # print(age >= 21)
# if (age >= 21) and (age2 >= 21):
#     print("Both ages pass the test.")
# else:
#     print("Somebody is under-age.")

# toppings = ['sausage', 'pepperoni', 'pineapple']
# choice = input("Enter a pizza topping => ")
# if choice in toppings:
#     print(f" {choice.title()} is an available option.")
# elif choice not in toppings:
#     print(f"No go for {choice.title()}.")

# namelist = []
#
# mystr = input("Enter a name => ")
# namelist.append(mystr)
#
# if namelist[0] == 'Kyle' or namelist[0].lower() == 'kyle':
#     print(f"{namelist[0].upper()} is almost 30.")
# elif namelist[0] != 'Kyle':
#     age = input("What's your age? => ")
#     print(f"{namelist[0].title()} is {age}.")

# mystr = "Kyle is almost 30."
# if mystr[0:5].strip() == 'Kyle' or mystr[0:5].lower().strip() == 'kyle':
#     print(f"His name is {mystr[0:5].upper()}.")
# else:
#     print("Not sure what that person's age is.")

# alien_color = 'green'
# choice = input("Enter a color => ")
# if choice.lower() == 'green':
#     print("You just earned 5 pts!")
# elif choice.lower() == 'yellow':
#     print("You just earned 10 pts!")
# elif choice.lower() == 'red':
#     print("You just earned 15 points")

# name = input("Enter your name => ")
# age = int(input("Enter an age => "))
# if age < 2:
#     print(f"{name} is a baby.")
# elif age >= 2 and age < 4:
#     print(f"{name} is a toddler.")
# elif age >= 4 and age < 13:
#     print(f"{name} is a kid.")
# elif age >= 13 and age < 20:
#     print(f"{name} is a teenager.")
# elif age >= 20 and age < 65:
#     print(f"{name} is an adult.")
# else:
#     print(f"{name} is an elder.")

# usernames = []
# existing_users = ['admin']
# while True:
#     get_name = input("enter some user names => ")
#     usernames.append(get_name)
#     if len(usernames) >= 5:
#         break
# print('\n')
#
# if len(usernames) >= 5:
#     for username in usernames:
#         if username.lower() in existing_users or username.title() in existing_users:
#             print(f"{username} has already been taken'\n'")
#         else:
#             print(f"Hey {username.title()} thanks for logging in.'\n")
# else:
#     print("Not enough names yet!")

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for number in number_list:
#     if number == 1:
#         print(str(number) + 'st', end=' ')
#     elif number == 2:
#         print(str(number) + 'nd', end=' ')
#     elif number == 3:
#         print(str(number) + 'rd', end=' ')
#     else:
#         print(str(number) + 'th', end=' ')
