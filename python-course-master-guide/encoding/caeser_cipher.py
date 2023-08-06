from random import randrange

from encoder_decoder import encode, decode


def caeser_encrypt_simple(message, offset=None):
    if offset is None:
        offset = randrange(1, 26)

    encoded = encode(message)
    encrypted = []
    for number in encoded:
        if not number == 32:
            number += offset
            if number > 122:
                number -= 26
        encrypted.append(number)

    encrypted_message = decode(encrypted)
    return encrypted_message, offset


def caeser_decrypt_simple(message, offset):
    encoded = encode(message)
    decrypted = []

    for number in encoded:
        if not number == 32:
            number -= offset
            if number < 97:
                number += 26
        decrypted.append(number)

    decrypted_message = decode(decrypted)
    return decrypted_message


def bruteforce(message):
    print("Brute forcing", repr(message))
    for offset in range(1, 26):
        print("Offset", offset, repr(caeser_decrypt_simple(message, offset)))


print("Encrypt, decrypt, or brute force?   e/d/b")
choice = input("> ")

print("Enter message:")
message = input("> ")

if choice == "e":
    encrypted_message, offset = caeser_encrypt_simple(message)

    print("Encrypted with an offset of", offset)
    print(repr(encrypted_message))


elif choice == "d":
    print("Enter offset:")
    offset = int(input("> "))

    decrypted_message = caeser_decrypt_simple(message, offset)

    print("Decrypted:", repr(decrypted_message))

elif choice == "b":
    bruteforce(message)
