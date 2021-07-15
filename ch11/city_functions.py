def get_location(city_name, country_name, population=''):
    if population:
        full_loc = f"{city_name}, {country_name}, Population: {population}"
    else:
         full_loc = f"{city_name}, {country_name}"
    return full_loc.title()