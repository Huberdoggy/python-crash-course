from classes import Restaurant, IceCreamStand as Ice


# restaurant = Restaurant('Bella Cucino', 'Italian')
# print(f"The new restaurant {restaurant.restaurant_name} has a variety of {restaurant.cuisine_type} delicacies.")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.number_served = 3000
# print(f"{restaurant.restaurant_name} has served {restaurant.number_served} people so far.")
# restaurant.people_served(3002)
# print(f"{restaurant.restaurant_name} has served {restaurant.number_served} people so far.")


blue_bunny = Ice('Happy Ice-Cream Truck', 'gourmet-gelatto')
blue_bunny.add_flavors()
blue_bunny.print_flavors()