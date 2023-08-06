string_length = "Print the length of the string."
print(string_length)
x = "The Python programming language."


print(len(x))


################################################################################


string_first_characters = "Check if the first 3 characters of the string are 'Hel'."
print(string_first_characters)
x = "Hello world."

y = "Hel"
if x[0:3] == y:
    print("Found")

if x[0] == y[0] and x[1] == y[1] and x[2] == y[1]:
    print("Found")


################################################################################


string_last_characters = "Check if the last 5 characters of the string are 'orld.'"
print(string_last_characters)
x = "Hello world"


################################################################################


counting_characters = "Find the number of times the letter 'e' appears in the string."
print(counting_characters)
x = "Python has a set of keywords that are reserved words that cannot be used as variable names."

print(x.count("e"))


################################################################################


converting_case = "Convert the string to upper case."
print(converting_case)
x = "abcdef"

print(x.upper())


################################################################################


converting_letters = "Convert just the first letter of each word to upper case."
print(converting_letters)
x = "the python programming language."

# print(x.capitalize())
# print(" ".join(map(str.capitalize, x.split())))

print(x.title())


################################################################################


breaking_up_strings = "Convert the string to a list of words."
print(breaking_up_strings)
x = "Python uses indentation to indicate a block of code"


print(x.split())


################################################################################


replacing_characters = "Replace all the spaces in the string with underscores _"
print(replacing_characters)
x = "Today is the 17th of Feburary."


print(x.replace(" ", "_"))


################################################################################


removing_characters = "Remove all the spaces from the string."
print(removing_characters)
x = "Today is the 17th of Feburary."


print(x.replace(" ", ""))


################################################################################


checking_position = "Print the position of the letter 'r' in the string."
print(checking_position)
x = "The Python programming language."

print(x.find("r"))
print(x.index("r"))


################################################################################


checking_contains = "Check if the string contains the word 'hello'."
print(checking_contains)
x = "A common string when testing code is 'hello world'."

if "hello" in x:
    print("Contains 'hello'")

if x.count("hello") > 0:
    print("Count > 0")


################################################################################


checking_simple = "Check if all characters in a string are numbers."
print(checking_simple)
x = "0123456789"

if x.isdecimal():
    print("All digits")
else:
    print("not all")


################################################################################


checking_complex = "Check if all the characters in a string are letters in the alphabet or spaces."
print(checking_complex)
x = "Does this contain any nonstandard characters"

is_valid = False
for character in x:
    if character.isalpha() or character.isspace():
        is_valid = True
    else:
        is_valid = False
        break

if is_valid:
    print("Yes!")
else:
    print("No.")


################################################################################
