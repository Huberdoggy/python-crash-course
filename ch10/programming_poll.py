from datetime import datetime
from os import stat
import sys


filename = 'textdocs/poll_responses.txt'
current_date = datetime(year=2021, month=7, day=10)
line_num = 1


def response_organizer(name, response):
    stored_response = {'Name': name.title(), 'Response': response}
    return stored_response


with open(filename, 'a+') as file_object:
    if stat(filename).st_size > 0:
        print("Existing contents in this file. Not adding heading..")
        sys.exit()
    else:
        print("Files is empty. Writing heading to file prior to commencing the poll...")
        heading = "**** POLL RESULTS ****"
        file_object.write(f"\t{heading}")

while True:
    print("You will be asked a series of questions for this poll"
          " (enter 'q' to quit) => ")
    p_name = input("First, what's your name? => ")
    if p_name == 'q':
        break
    else:
        print(f"Thank you for your response {p_name}!")
        poll_response = input("And why do you like programming? (enter 'q' to opt out) => ")
        if poll_response == 'q':
            break
        else:
            full_response = response_organizer(p_name, poll_response)
            with open(filename, 'a+') as file_object:
                file_object.write(f"\n{line_num} - {full_response} was added to the poll results on {current_date}")
                line_num += 1
