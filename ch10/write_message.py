filename = "textdocs/programming.txt"

# Append mode is 'a' write mode is 'w' NOTE: write mode erases existing contents when opening
with open(filename, "a") as file_object:
    file_object.write(
        "\tI am learning about various data manipulation features in Py\n"
    )
    file_object.write("\tSuch as appending to files")
