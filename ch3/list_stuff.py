import sys

bikes = ["trek", "cannondale", "redline", "specialized"]
print(bikes[2].title())
print(bikes[0:2])
print(bikes[-1])

message = f"My first bike was a {bikes[2].title()}"
print(message)

names = ["Paul", "Stephen", "Jenna", "Renae"]
count = 1
for name in names:
    if name == "Paul":
        print(f"Family member {count} is named: {name}. Hey dad.")
    elif name == "Stephen":
        print(f"Family member {count} is named: {name}. Hey brotha'.")
    elif name == "Jenna":
        print(f"Family member {count} is named: {name}. HEY SOUL SISTA!")
    else:
        print(f"Family member {count} is named: {name}. Whatsup mom?")
    count = count + 1

carList = ["camaro", "civic", "audi"]
for car in carList:
    print(f"One of my previous cars was a {car.title()}")
carList.append("Pontiac")
print(carList.index("Pontiac"))
del carList[0]
print(carList)
popped_car = carList.pop(0)
print(carList)
print(popped_car)

guestList = ["Paul", "Renae", "Stephen", "Jenna"]
count = 1
for guest in guestList:
    global cant_make
    if guest == "Paul":
        print(f"Guest {count} is named: {guest}. Hey dad.")
    elif guest == "Stephen":
        print(f"Guest {count} is named: {guest}. Hey brotha'.")
    elif guest == "Jenna":
        print(f"Guest {count} is named: {guest}. HEY SOUL SISTA!")
        cant_make = guestList.pop(-1)
    else:
        print(f"Guest {count} is named: {guest}. Whatsup mom?")
    count += 1


print(
    f"{cant_make} apparently can't make it. So now the guest list is: {guestList}"
)
print("I guess there's only room for me to invite 2")
for remaining in guestList:
    if remaining == "Paul":
        print(f"Sorry dad, you'll have to go..")
        guestList.remove(remaining)
    if len(guestList) >= 2:
        print(f"Can't fit you in here either mom..sowwy")
        del guestList[0:2]
print(f"Looks like I'm the only one left => {guestList}")

countryList = ["America", "Saudi-Arabia", "United Kingdom", "China"]


def formatList(country):
    country.sort()
    print(country)
    country.sort(reverse=True)
    print(country)
    print(len(country))
    print(f"And the sorted variant is: {sorted(countryList)}")
    reversed(countryList)
    print(f"And the reverse variant is: {countryList}")
    return country


i = input("Please enter a list to sort: => ")
if i == "countryList":
    formatList(countryList)
else:
    print(f"No data matches {i}")
    sys.exit()
