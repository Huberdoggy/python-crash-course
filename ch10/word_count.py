from os import stat

doc_list = []
prefix = ""
suffix = ".txt"


def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist..")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"\n\tThe file {filename} has about {num_words} words.\n")


while True:
    print(
        "Enter a filename and I will count the words"
        " (the '.txt' has been automatically included for you."
    )
    choice = input("(or 'q' to quit and stop adding files) => ")
    if choice == "q":
        break
    prefix = "textdocs/{0}{1}".format(choice, suffix)
    try:
        if stat(prefix).st_size > 0:
            print(f"File name is not empty. Just to inform you..")
    except FileNotFoundError:
        print("Cant find that one..")
        break
    else:
        doc_list.append(prefix)
        print(f"Now adding {prefix} to list")
        print(doc_list)
        prefix = ""
print(f"\n\t***THE WORD COUNT OF BOOKS IN THE LIST***")
for doc in doc_list:
    count_words(doc)
