filename = "textdocs/learning_python.txt"

with open(filename) as file_object:
    # for line in file_object:
    #     print(line.strip())
    lines = file_object.readlines()

lower_c = "c sharp"
# sep_string = ''
for line in lines:
    rep_line = line.replace("Python", lower_c.upper())
    print(rep_line)

#     sep_string += line.strip()
# print(f"{sep_string}")
# print(len(sep_string))
