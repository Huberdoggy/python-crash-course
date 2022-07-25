from datetime import datetime

filename = "textdocs/guest_book.txt"
current_date = datetime(year=2021, month=7, day=10)
line_num = 1

while True:
    prompt = input("Please enter your name" " (or enter 'q' to quit) => ")
    if prompt != "q":
        name = prompt
        print(f"Hello there {name.title()}!")
        with open(filename, "a+") as file_object:
            file_object.write(
                f"\n{line_num} - {name.title()} was logged as using the program on {current_date}"
            )
            line_num += 1
    else:
        break
