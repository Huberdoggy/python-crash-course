# ## MESSAGE
def display_message():
    """INFORM EVERYONE WHAT I'M LEARNING ABOUT IN PYTHON"""
    print("Today, I'm learning about functions.")


# MORE MESSAGES
def send_messages(orig_messages, finished_messages):
    while orig_messages:
        current_message = orig_messages.pop()
        print(f"Sending message: {current_message}")
        finished_messages.append(current_message)


def show_sent_messages(original_messages, finished_messages):
    print('-' * 40)
    print(f"\nORIGINAL MESSAGES ARE:\n")
    for message in original_messages:
        print(f"\t{message}")
    transfer_result = f"\nThe following messages have been sent:\n"
    print(transfer_result.upper())
    for message in finished_messages:
        print(f"\t{message}")


# FAVORITE BOOK
def favorite_book(title):
    print(f"One of my favorite books is {title}.")


# T-SHIRT
def make_shirt(size='large', text='I love python'):
    print(f"This shirt is a {size} sized item."
          f" And the logo says {text.title()}.")


# CITIES
def describe_city(city_name, country='usa'):
    if country == 'usa':
        print(f"{city_name.title()} is in THE {country.upper()}")
    else:
        print(f"{city_name.title()} is in {country.title()}.")


# ALBUM
def make_album(artist_name, album_title, num_of_songs=None):
    """RETURNS A DICTIONARY OF INFORMATION REGARDING MUSIC ALBUMS.
    BASED ON USER INPUT. OPTIONAL - NUMBER OF SONGS"""
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if num_of_songs:
        album['songs'] = num_of_songs
    return album


# SANDWICHES
def make_sandwich(bread, *ingredients):
    """Summarize the sandwich we're about to create"""
    print(f"\nMaking a sandwich with the following ingredients:")
    sandwich = {'bread': bread, 'ingredients': ingredients}
    return sandwich


# CARS
def make_car(manufacturer, model, **misc_info):
    """Build a dictionary containing everything we know about the car."""
    misc_info['manufacturer'] = manufacturer
    misc_info['model'] = model
    return misc_info
