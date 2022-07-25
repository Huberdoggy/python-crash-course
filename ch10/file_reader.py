# Use 'with' syntax to have Python automatically close the file. This prevents isues with improper
# calls to 'close()' manually, as specified in Chapter 10

filename = "textdocs/pi_million_digits.txt"
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip()) # remove final blank line after 'read' as well as newline returns from print
# print(f"\n" + '-' * 25)

# Storing lines from file in a list
with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
# print(f"\n" + '-' * 25)

# Concat
pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter you birthday in the form mmddyy => ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does NOT appear in the first million digits of pi...")
# print(f"{pi_string[:52]}...")
# print(len(pi_string))
