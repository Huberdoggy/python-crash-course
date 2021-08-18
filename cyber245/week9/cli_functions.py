from secrets import api_key

def make_menu(opt1, opt2, opt3):
    """Make a numeric option menu for the user
    Run as an infinite loop in main.py until 'quit' is chosen"""
    my_dict = {1: opt1,
               2: opt2,
               3: opt3,}
    return my_dict


def build_request_url(city, state, units="&units=imperial"):
    """Consolidate work in main.py by creating a concatenated string,
    which will take input variables to construct the full URL for our endpoint request"""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + str(city) + "," + str(state) + ",us" + units + "&appid=" + api_key
    return complete_url


def print_the_weather(curr_temp, curr_pressure, curr_humidity, w_description):
    print("\n")
    print(f"\tCURRENT FORECAST AT LOCATION")
    print(f"\t" + "-" * 30)
    print(f"\tTemperature in Fahrenheit: {str(curr_temp)} degrees\n"
          f"\tAtmospheric pressure is: {str(curr_pressure)}\n"
          f"\tHumidity is: {str(curr_humidity)}%\n"
          f"\tForecast is showing: {str(w_description)}")
    print("\t" + "-" * 30 + "\n")
