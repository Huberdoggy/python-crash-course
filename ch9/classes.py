# Classes are generally denoted with caps like =>
# class Human:
#     """A simple attempt to model a person"""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#
#     def run(self):
#         """Simulate a person running"""
#         print(f"{self.name} is now running fast!")
#
#     def shake_hand(self):
#         """Simulate a greeting formality"""
#         print(f"{self.name} is shaking their hand as a courtesy.")
#
#
# person_1 = Human('Kyle', 29)
# print(f"The first person created is named {person_1.name}\n"
#       f"And his age is {person_1.age}.")
# print("-" * 100)
# person_1.run()
# person_1.shake_hand()
#
# person_2 = Human('Paul', 55)
# print("-" * 100)
# print(f"The next person created is named {person_2.name}\n"
#       f"And his age is {person_2.age}.")

# RESTAURANTS


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is named {self.restaurant_name}.")
        print(f"The current menu includes {self.cuisine_type} food.")

    def open_restaurant(self):
        print(
            f"The restaurant {self.restaurant_name} is now open for business!!"
        )

    def people_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print(f"You can't go back in time! Rejecting {number}.")
            print(
                f"The current total number of people served is still {self.number_served}."
            )


# ICE CREAM STAND ADDITION


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self):
        flavor_list = []
        while len(flavor_list) < 6:
            choose = input(
                "Enter some ice-cream flavors"
                " Or enter 'q' to quit any time => "
            )
            if choose == "q":
                break
            if len(flavor_list) == 6:
                break
            elif len(flavor_list) < 6:
                flavor_list.append(choose)
                if len(flavor_list) >= 3 and len(flavor_list) < 6:
                    ask = input("Still want to add more? (y/n) => ")
                    if ask == "n":
                        break

        for flavor in flavor_list:
            self.flavors.append(flavor)

    def print_flavors(self):
        print("-" * 50)
        print("****FLAVOR INVENTORY****" + "\n")
        print("The Blue Bunny truck has:\n\t")
        for flavor in self.flavors:
            print(f"{flavor.title()}")


# USERS AND LOGIN ATTEMPTS
class User:
    def __init__(self, first_name, last_name, age, hair_color, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.login_attempts = login_attempts

    def describe_user(self):
        print(
            f"\tMy name is {self.first_name} {self.last_name}\n"
            f"\tI am {self.age}, and my hair color is {self.hair_color}."
        )

    def greet_user(self):
        print(
            f"\nHello there {self.first_name} {self.last_name}!! I really like your {self.hair_color} hair!"
        )

    def increment_login_attempts(self, count):
        if self.login_attempts >= 0 and count > 0:
            self.login_attempts += count
            print(f"{count} added successfully")
        elif count < 0:
            print("Can't accept a negative value for login attempts.")
        elif count == 0:
            print(f"Please enter an int greater than {count}")
        print(
            f"Current login attempts for {self.first_name}: {self.login_attempts}"
        )

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(
            f"Reset login attempts. Current login attempts for {self.first_name} is {self.login_attempts}"
        )


class Privileges:
    def __init__(self):
        self.privileges = ["can add user", "can delete user", "can ban user"]

    def show_privileges(self):
        print(f"The Admin has the following elevated permissions:")
        for privilege in self.privileges:
            print(f"\n\t{privilege.upper()}")


class Admin(User):
    def __init__(self, first_name, last_name, age, hair_color, login_attempts):
        super().__init__(
            first_name, last_name, age, hair_color, login_attempts
        )
        self.privileges = Privileges()


# MANIPULATING A CAR CLASS WITH A DEFAULT VALUE


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make}, {self.model}, {self.year}."
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # Write a method to dynamically update the given attribute when called
    def update_odometer(self, mileage):
        """Set the mileage to the given vaule
        And reject changes if they attempt to roll back the odometer reading
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(
                f"You can't rollback an odometer! Rejecting number {mileage}"
            )

    def increment_odometer(self, miles):
        """Add the given amt to the odometer reading"""
        self.odometer_reading += miles


#
# # Modularize 'battery' into its own class to prevent clutter in 'ElectricCar'
class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Init the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        print(f"This car can go about {car_range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            old_bat = self.battery_size
            self.battery_size = 100
        print(
            f"Battery size was set to {old_bat}, but now it's {self.battery_size}"
        )


# # Define a child class which inherits from 'Car'
class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Init attributes of the parent class"""
        super().__init__(make, model, year)
        """Then init attribs special to this class"""
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement describing battery size"""
    #     print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
