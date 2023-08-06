simple_open_close = "Open and close the file 'file.txt'"
print(simple_open_close)

file = open("file.txt")
file.close()


################################################################################


context_open_close = "Open the file 'file.txt' using the advanced context manager."
print(simple_open_close)

with open("file.txt") as file:
    pass


################################################################################


read_contents_into_string = "Read everything in file into a single string."
print(read_contents_into_string)

file = open("file.txt", "r")
contents = file.read()
file.close()
print(contents)


################################################################################


read_contents_into_list = "Read everything in the file into a list of strings."
print(read_contents_into_list)

file = open("file.txt", "r")
contents = file.readlines()
file.close()
print(contents)


################################################################################


read_contents_and_split = "Read everything into a string and then split into a list of strings."
print(read_contents_and_split)

file = open("file.txt", "r")
contents = file.read().splitlines()
file.close()
print(contents)


################################################################################


open_and_iterate = "Open the file and iterate over each of the lines and print them."
print(open_and_iterate)


file = open("file.txt", "r")
for line in file:
    print(line)


################################################################################


simple_write = "Write the string 'x' to a new file 'simple_write.txt"
print(simple_write)
x = "This is a test output"


################################################################################


complex_write = "Write the list of strings 'x' to a new file 'complex_write.txt'. Have each string appear on a separate line."
print(complex_write)
x = [
    "This should be line number 1.",
    "This should be line number 2.",
    "This should be line number 3."
]


################################################################################


writing_non_strings = "Write the list of integers 'x' to a file. Put a semicolon ';' between each integer in the file 'integers.txt'."
print(writing_non_strings)
x = [4, 8, 15, 16, 23, 42]


################################################################################


adding_to_file = "Add the string 'x' to the end of the file 'file.txt'. Do not delete the previous contents of the file."
print(adding_to_file)
x = "This should appear at the end!"


################################################################################
