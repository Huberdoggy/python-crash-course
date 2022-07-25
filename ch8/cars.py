from functions import make_car as mc

car_profile = mc(
    "Chevy", "Camaro", location="Colorado", color="Black n' Yellow"
)
print(f"\n\t***CUSTOM CAR***")
for key, value in sorted(car_profile.items()):
    print(f"\n\t{key.title()}: {value.title()}")
