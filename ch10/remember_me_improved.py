import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'textdocs/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'textdocs/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        check = input(f"Is this {username} running the program? (y/n)? ")
        if check == 'y':
            print(f"Welcome back, {username}!")
        elif check == 'n':
            username = get_new_username()
            print(f"Got it! Thanks for clarifying that {username}. I've updated the record")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
