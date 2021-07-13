import json

def get_number(number):
    file_name = 'textdocs/fav_num.json'
    try:
        with open(file_name) as f:
            contents = f.readlines()
            for item in contents:
                # Have to strip the literal double quotes from 'item' for this to work
                existing_num = item.strip('""')
                if existing_num == number:
                  return existing_num
    except FileNotFoundError:
        with open(file_name, 'w') as f:
            json.dump(number, f)
            print(f"We'll remember your favorite number is {number} when you return.")
            return None


user_num = input("Enter your favorite number (or 'q' to quit) => ")
if user_num == 'q':
    print("Okay, exiting the program...")
else:
    existing_num = get_number(user_num)
    if existing_num:
        print(f"I already know your favorite number. It's {existing_num}")
    else:
        pass

