import json
import os
import re
import sys
from os import name

from termcolor import colored

suffix = ".txt"


def add_to_path(path_str):
    count = 1
    for i in range(0, 2):
        sys.path.insert(count, path_str[i])
        count += 1


def expand_env_vars():  # To keep it open, I wanted to expand the env var for 'Documents' depending on the
    # context where the user's running the program. Instead of blindly typing base directories and preventing typos,
    # this way, we can start in /home/'username'/Documents and customize a file name from there
    if name == "nt":
        return os.path.expandvars("C:\\Users\\$USERNAME\\Documents\\")
    else:
        return os.path.expandvars("$HOME/Documents")


def does_fpath_exist(path_str, pattern_dict):
    if os.path.isdir(path_str):
        while True:
            # Technically, this will only go until a file-name matches my
            # naming convention, since it will return 'filename' at that point
            filename = input(
                f"Will store your file under {colored(path_str, 'green')}.\n"
                f"Please enter a file name (or 'q' to quit) => "
            )
            if filename == "q":
                print("Come back soon. Good-bye!")
                sys.exit(0)
            elif re.fullmatch(
                pattern_dict.get("filename_input", "empty"), filename.strip()
            ):
                if name == "posix":
                    full_f_path = path_str + "/" + filename.strip() + suffix
                    print(
                        f"\nDetected a "
                        + colored("Linux", "green")
                        + " operating system."
                        f"\nFull file path will be: {colored(full_f_path, 'green')}"
                    )
                    return full_f_path
                else:
                    full_f_path = (
                        path_str + filename.strip() + suffix
                    )  # Take out that forward slash
                    print(
                        f"\nDetected a "
                        + colored("Windows", "green")
                        + " operating system."
                        f"\nFull file path will be: {colored(full_f_path, 'green')}"
                    )
                    return full_f_path
            else:
                print(
                    colored(
                        f"File naming convention for {filename.strip()} is invalid.",
                        "red",
                    )
                )
    else:
        print(colored(f"Input directory {path_str} does NOT exist.", "red"))
        return None


def store_data(
    file_name, user_info
):  # take input vars and the full file path from above function.
    with open(file_name, "w") as f:
        json.dump(user_info, f)
    print(colored(f"Successfully dumped to {file_name}", "green"))
    with open(file_name) as f:
        info_dict = json.load(f)
        line = ""  # I'm doing this so that I can construct a 'return' with the full formatted info sep by \n
        for key in info_dict:
            line += f"\t\t\t{key}: {info_dict[key]}\n"
        return f"\n\t*** CURRENT CONTENTS OF: {colored(file_name, 'green')} ***\n\n{line}"
