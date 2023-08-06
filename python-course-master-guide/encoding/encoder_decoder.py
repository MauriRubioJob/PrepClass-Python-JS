
def encode(message):
    numbers = []
    for character in message:
        number = ord(character)
        numbers.append(number)
    return numbers


def decode(numbers):
    characters = []
    for number in numbers:
        character = chr(number)
        characters.append(character)
    message = "".join(characters)
    return message


if __name__ == "__main__":
    print("Enter message:")
    message = input("> ")

    encoded = encode(message)
    print("Encoded:", encoded)
