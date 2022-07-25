# pizzas = ['cheese', 'hawiaan', 'sausage', 'pepperoni']
# # for pizza in pizzas:
#     # print(f"I eagerly look forward to eating {pizza.upper()}\n")
# pizzas.insert(1, 'tofu')
# friends_pizzas = pizzas[:]
# friends_pizzas.append('bacon')
# # print(pizzas)
# # print(friends_pizzas)
# print("My favorite pizzas are: =>'\n'")
# for pizza in pizzas:
#     print(f"I like {pizza}.")
# print('\n\n')
# for pizza in friends_pizzas:
#     print(f"Friend likes {pizza}.")


#
# print("They are all tastey.")
#
# animals = ['dog', 'cat', 'wabbit', 'mouse', 'kangaroo', 'Skippy']
# for animal in animals:
#     if animal == 'dog':
#         print(f"A {animal} is man's best friend.")
#     elif animal == 'cat':
#         print(f"A {animal} has traditionally been revered in many cultures.")
#     else:
#         print(f"We can go {animal} hunting. But they can be domesticated.")
#
# print('\n' + "All of these could be MY pet.")
# print(f"The first 3 items in the animals list are: {animals[:3]}")
# print(f"The three middle items are: {animals[1:4]}")
# print(f"And the last 3 items in the animals list are: {animals[-3:]}")

# squares = []
# for i in range(1, 11):
#     i **= 2
#     squares.append(i)
#
# print(squares)

# OR
#
# squares = []
# for i in range(1, 11):
#     squares.append(i ** 2)
#
# print(squares)

# oddList = []
# for i in range(1, 21, 2):
#     print(i)


# cubes = []
# for i in range(1, 11):
#     cubes.append(i ** 3)
#     print(i ** 3)
#
# print(cubes)


# LIST COMPREHENSION STYLE
#
# cubes = [value ** 3 for value in range(1, 11)]
# print(cubes)

# TUPLES - Immutable unless the variable is reassigned

# foods = ('apple', 'pear', 'lasagna', 'cheese')
# for food in foods:
#     print(f"{food}", end=' ')
# print('\n' * 2)
# foods = ('apple', 'pear', 'mac n\' cheese', 'alfredo')
# for food in foods:
#     print(f"{food}", end=' ')
