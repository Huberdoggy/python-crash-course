from classes import Car, ElectricCar, Battery

my_tesla = ElectricCar("tesla", "model s", 2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
print(f"My special car class is a {my_tesla.get_descriptive_name()}")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
