
# To convert from a character to it's ASCII encoding
#     ord( character_to_convert )


# To convert from an integer to it's ASCII character
#     chr( int_to_convert )


character = "a"
number = ord(character)
print(character, number)

character = "A"
number = ord(character)
print(character, number)

character = "ñ"
number = ord(character)
print(character, number)

number = 30451
character = chr(number)
print(number, character)
