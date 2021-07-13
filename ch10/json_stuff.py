import json
import sys


def data_store(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f)
    print(f"Successfully dumped to {file_name}")
    with open(file_name) as f:
        users = json.load(f)
        for name in sorted(users):
            print(f"Welcome back {name.title()}!\n")


suffix = '.json'
usernames = []

print("Enter some usernames and I will store them as JSON objects in a file"
                     " (press 'q' to quit)")
while True:
    add_user = input("Name? => ")
    if add_user == 'q':
        break
    else:
        print(f"Thanks for that info. We'll remember you when you come back {add_user}")
        usernames.append(add_user)

if len(usernames) == 0:
    print("No existing data to dump")
    sys.exit()
else:
    chosen_file = input("Now, enter a filename to dump the usernames you've provided: ")
    full_file_name = 'textdocs/{0}{1}'.format(chosen_file, suffix)
    data_store(usernames, full_file_name)

