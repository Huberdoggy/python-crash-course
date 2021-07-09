from classes import Car

new_car = Car('audi', 'a6', '2016')
print(new_car.get_descriptive_name())
new_car.update_odometer(15_000)
new_car.read_odometer()
# # new_car.increment_odometer(200)
# # # new_car.update_odometer(50)
# # new_car.read_odometer()