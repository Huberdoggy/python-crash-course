"""Use the 'count' method to iterate through a text file and find how many
    occurrences of the word 'the' appear. Will user lower() method to include case
    sensitivity"""

suffix = '.txt'


def occurence_check(filename, word_to_check):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist..")
    else:
        words = contents.split()
        count = 0
        for word in words:
            lower_word = word.lower()
            title_word = word.title()
            target_word = word_to_check
            # Just covering my bases here after some trial and error. Might not be needed
            if target_word == lower_word or target_word == title_word:
                count += 1
        return count


file = input("Enter a filename: ")
full_path = 'textdocs/{0}{1}'.format(file, suffix)
your_word = input(f"Now, enter a word, and I will see how man times it appears in {full_path}: ")
num_of_occurrences = occurence_check(full_path, your_word)
print(f"\n\tThe file has about {num_of_occurrences} occurrences of the word '{your_word}'.")

