# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# To start with an empty dict
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)
#
# kyle = {'x_pos': 0, 'y_pos': 25, 'speed': 'fast'}
# print(f" Original position : {kyle['x_pos']}")
#
# # Move Kyle to the right
# # Determine how far to move him based on his current speed
# # if kyle['speed'] == 'slow':
# #     x_increment = 1
# # elif kyle['speed'] == 'medium':
# #     x_increment = 2
# # else:
# #     # He's fast
# #     x_increment = 3
# #
# # # The new position is the old position plus the increment
# # kyle['x_pos'] += x_increment
# # print(f" New position: {kyle['x_pos']}")

# favorite_languages = {
#     'kyle': 'python',
#     'stephen': 'visual-basic',
#     'jenna': 'french',
#     'renae': 'spanish',
# }
#
# if 'erin' not in favorite_languages.keys():
#     print("Erin please get in this group.")

# Use sorted method for ordering...
#
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}\t What is up?")

# Only the values...
# print("The following languages have been mentioned: ")
# for language in sorted(favorite_languages.values()):
#     print(f"{language.title()}", end=' ')

# people = {
#     'scott',
#     'kyle',
#     'tony',
# }
# #
# for name in favorite_languages.keys():
#     #print(name.title())
#     if name in people:
#         target_lang = favorite_languages[name].title()
#         print(f"\t{name.title()} I see you really like {target_lang}!")

# language = favorite_languages['kyle'].title()
# print(f"Kyle's favorite language is \n\t{language.upper()}!!")
# bro_lang = favorite_languages.get('stephen', 'No such person')
# print(bro_lang)

# for name, lang in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language is: {lang.title()}")
#
# # Or just the key...
# for name in favorite_languages.keys():
# # This is the default for dict loops so you could just write "for name in favorite_languages:"
#     print(name.title())

# prog_words = {
#     'variable': 'a container',
#     'function': 'reusable code',
#     'if-else': 'executes based on logic',
#     'pep8': 'python syntax standard',
#     'pyenv': 'a great Python version manager',
# }
#
# for word, value in prog_words.items():
#     print(f"{word.upper()}:\n\t{value.title()}")

# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'sein': 'france',
# }
#
# for river, country in sorted(rivers.items()):
#     if str(country).lower() == 'united states':
#         print(f"The {river.title()} is in THE: {country.upper()}.")
#     else:
#         print(f"The {river.title()} is in: {country.upper()}.")

# fav_languages = {
#     'kyle': 'python',
#     'stephen': 'visual-basic',
#     'jenna': 'french',
#     'renae': 'spanish',
# }
#
# voters = [
#     'kyle',
#     'bob',
#     'billy',
#     'stephen',
#     'renae',
#     'jenna',
# ]
#
# for name in sorted(voters):
#     if name in fav_languages:
#         voter_lang = fav_languages[name]
#         print(f"Thanks for voting {name.title()} I can see you really like {voter_lang.upper()}!")
#     elif name not in fav_languages:
#         print(f"{name.title()} you should really cast your vote!")

# Nesting and Looping for mass efficiency...
#
# dogs = []
#
# # Make 20 pink dogs
# for dog_num in range(20):
#     new_dog = {
#         'color': 'pink',
#         'breed': 'poodle',
#         'speed': 'fast',
#         'weight': 'skinny',
#     }
#     dogs.append(new_dog)
# #
# # # Show the first 5 dogs..
# # for dog in dogs[:5]:
# #     print(dog)
# # print("-" * 20)
#
# # print(f"Total number of dogs: {len(dogs)}")
#
# for dog in dogs[:3]:
#     if dog['color'] == 'pink':
#         dog['color'] = 'brown'
#         dog['breed'] = 'chuahua'
#         dog['speed'] = 'slow'
#         dog['weight'] = 'fat'
#
# print(f"The first 3 dogs have been modded =>\n")
# for dog in dogs[:3]:
#     print(dog)

# Enhanced scripts from above using Nesting.....

# pasta = {
#     'noodles': 'italian',
#     'toppings': ['white-cheddar', 'shrimp', 'roma-tomatoes'],
# }
#
# # Summarize the order
# print(f"Kyle, you ordered {pasta['noodles'].title()} noodles.")
# print("-" * 35)
# print("And here are your desired toppings => ")
# for topping in pasta['toppings']:
#     print(f"\t {topping}")

# fav_languages = {
#     'kyle': ['python', 'c-sharp', 'bash'],
#     'renae': ['spanish', 'french'],
#     'jenna': ['japenese'],
#     'stephen': ['excel', 'visual-basic', 'powershell'],
# }
#
# for name, languages in fav_languages.items():
#     if len(languages) > 1:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"{language.title()}")
#     elif len(languages) == 1:
#         print(f"\n{name.title()} really likes {language.upper()}. Only that one.")



## MORE PRACTICE....

# people = {
#     'paul': {
#         'last': 'huber',
#         'pants': 'jeans',
#         'shirt': 'Jim\'s Market',
#     },
#     'stephen': {
#         'last': 'huber',
#         'pants': 'khaki',
#         'shirt': 'Edward Jones',
#     }
# }
#
# for name, info in people.items():
#     print(f"\nHis name is: {name.title()}")
#     if info['shirt'] == 'Jim\'s Market':
#         full_clothes = f"{info['pants']} and a {info['shirt']} shirt."
#     elif info['shirt'] == 'Edward Jones':
#         full_clothes = f"{info['pants']} pants and AN {info['shirt']} button-up shirt."
#     surname = info['last']
#
#     print(f"\tHe's wearing: {full_clothes}")
#     print(f"\tHis last name is: {surname.title()}")

# pets = []
# print(pets)
#
# pet_1 = {'name': 'garfield', 'type': 'cat', 'owner': 'bud'}
# pet_2 = {'name': 'roger', 'type': 'dog', 'owner': 'tiffany'}
# pet_3 = {'name': 'fluffy', 'type': 'gerbil', 'owner': 'paul'}
#
# pets.append(pet_1)
# pets.append(pet_2)
# pets.append(pet_3)
#
# for pet in pets:
#     if pet['name'] == 'garfield':
#         pet['name'] = pet['name'].upper()
#         pet['owner'] = pet['owner'].upper()
#     else:
#         pet['name'] = pet['name'].title()
#         pet['owner'] = pet['owner'].title()
#     print(f"\n{pet}")
#
# cities = {
#     'sao paulo': {
#         'country': 'brazil',
#         'population': '5,000,000',
#         'fact': 'has a statue of Christ',
#     },
#     'los angeles': {
#         'country': 'usa',
#         'population': '2,000,000',
#         'fact': 'home of the Microsoft Center',
#     },
#     'minneapolis': {
#         'country': 'usa',
#         'population': '300,000',
#         'fact': 'is really cold',
#     },
# }
# title_str = "kyle's city table"
# print(f"{title_str.upper()}")
# print('-' * 35)
#
# for city, info in sorted(cities.items()):
#     print(f"The name of the city is: {city.title()}.")
#     for detail in info:
#         if str(detail) == 'country':
#             print(f"The name of the country is {info['country'].upper()}.")
#         elif str(detail) == 'population':
#             print(f"The approximate population is:\t{info['population']}.")
#         elif str(detail) == 'fact' and city.lower() == 'sao paulo' or city.lower() == 'minneapolis':
#             print(f"One fun fact is this city {info['fact']}.")
#         elif str(detail) == 'fact' and city.lower() == 'los angeles':
#             print(f"L.A is the {info['fact']}.")
#     print('-' * 35)

