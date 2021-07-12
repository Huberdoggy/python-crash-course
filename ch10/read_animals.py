"""Attempt to read from textdocs/[cats.txt][dogs.txt]
    and print to screen. Throw a customized error message if FileNotFound"""
from re import search

def check_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist..")
    else:
        words = contents.split('\n')
        if search('cat', filename):
            animal = 'cat'
            print(f"\n\tThe file {filename} has a {animal} named:")
            for word in words:
                print(f"\n\t{word}\n")
        elif search('dog', filename):
            animal = 'dog'
            print(f"\n\tThe file {filename} has a {animal} named:")
            for word in words:
                print(f"\n\t{word}\n")


print("\t------FILE 1-------")
check_file('textdocs/cats.txt')
print("\n\t------FILE 2-------")
check_file('textdocs/dogs.txt')
check_file('textdocs/dont_exist.txt')
