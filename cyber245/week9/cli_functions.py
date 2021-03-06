import re
import sys
from secrets import api_key

import requests
from termcolor import colored


def add_to_path(path_lst):
    count = 1
    for value in path_lst:
        sys.path.insert(
            count, path_lst[value]
        )  # Pull out the string path arg from 'key'
        count += 1


def compile_patterns(pattern_dict):  # Modified this to pass dic and
    # follow proper method of compiling raw regex - stored in new returned dict
    new_dict = {}
    for str_pattern in pattern_dict:
        try:
            raw_reg = re.compile(rf"{pattern_dict[str_pattern]}")
            new_dict[str_pattern] = raw_reg
            # return new_dict
        except re.error:
            print(f"Invalid regex expression {pattern_dict[str_pattern]}")
    return new_dict


def make_menu(opt1, opt2, opt3, opt4=None):
    """Make a numeric option menu for the user
    Run as an infinite loop in main.py until 'quit' is chosen"""
    my_dict = {
        1: opt1,
        2: opt2,
        3: opt3,
    }
    if opt4:
        my_dict[4] = opt4
    return my_dict


def build_request_url(city, state, units="&units=imperial"):
    """Consolidate work in main.py by creating a concatenated string,
    which will take input variables to construct the full URL for our endpoint request"""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = (
        base_url
        + "q="
        + city
        + ","
        + state
        + ",us"
        + units
        + "&appid="
        + api_key
    )
    return complete_url


def build_request_url_zip(zip, units="&units=imperial"):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = (
        base_url + f"zip={zip}" + ",us" + units + "&appid=" + api_key
    )
    return complete_url


def make_request(full_url):
    j_value_copies = (
        {}
    )  # will hold copied values to return for plugging into printing function
    try:
        response = requests.get(full_url)
        j_response = (
            response.json()
        )  # 'response' now holds a lst of nested dictionaries
        # from the endpoint. We will check if the 'cod' key
        # equals 404 - the web request status code for 'resource not found'
        if ["cod"] != "404":
            print(colored(f"\nCONNECTION TO ENDPOINT SUCCESSFUL!", "green"))
            nested_1 = j_response[
                "main"
            ]  # Here, 'main' is an object of interest to me
            # returned by the request -> it's a nested dict
            # which holds useful data...in particular 'temperatures'
            # I know the below solution probably isn't optimal but it works and helps clean up 'main.py'
            current_temp = nested_1["temp"]
            j_value_copies["temp"] = current_temp
            current_pressure = (
                float(nested_1["pressure"]) * 0.01450377
            )  # Convert hPa units to psi for convenience
            j_value_copies["pressure"] = current_pressure
            current_humidity = nested_1["humidity"]
            j_value_copies["humidity"] = current_humidity
            # Now, traverse up to the 'weather' info
            w = j_response["weather"]
            # 'Weather description is located at [weather][0]
            weather_desc = w[0]["description"]
            j_value_copies["description"] = weather_desc
            # print_the_weather(current_temp, current_pressure, current_humidity, weather_desc)
            return j_value_copies
        else:
            print("Data not found.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error retrieving data...exiting.")
        raise sys.exit(e)


def print_the_weather(j_dict):
    print("\n")
    print(f"\tCURRENT FORECAST AT LOCATION")
    print(f"\t" + "-" * 30)
    print(
        f"\tTemperature in Fahrenheit: {str(j_dict['temp'])} degrees\n"
        f"\tAtmospheric pressure (in psi) is: {j_dict['pressure']:.1f}\n"
        f"\tHumidity is: {str(j_dict['humidity'])}%\n"
        f"\tForecast is showing: {str(j_dict['description'])}"
    )
    print("\t" + "-" * 30 + "\n")
