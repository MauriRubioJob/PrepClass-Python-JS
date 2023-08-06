# Create a version of the game "Hangman".

# Requirements:
# 	- A word/phrase should first be entered, use
#       the "getpass" module to do so.
# 	- Allow only lowercase letters and spaces, no symbols or numbers.
# 	- The player has 10 guesses before gameover.

import getpass


def getphrase():
    while True:
        print("Enter phrase to guess:   (no numbers or symbols)")
        phrase = getpass.getpass("")

        phrase = phrase.lower()
        for char in phrase:
            if not char.isalpha() and not char.isspace():
                print("Error. Invalid character",
                      repr(char), "please try again.")
                exit()
        else:
            break

    return phrase


def get_guessed_phrase(guesses, phrase):
    guessed_phrase = phrase
    for letter in phrase:
        if letter.isalpha() and letter not in guesses:
            guessed_phrase = guessed_phrase.replace(letter, "_")

    return guessed_phrase


def input_guess():
    guess = input("Choose a letter: ")
    guess = guess.lower()
    if guess in guesses:
        print("You have already guessed this")
    elif guess.isalpha() and len(guess) == 1:
        guesses.append(guess)
    else:
        print("You have not guessed one letter")


def check_lives(lives):
    last_guess = guesses[-1]
    if last_guess not in phrase:
        lives = lives - 1
        print("Incorrect guess")
    elif last_guess in phrase:
        print("Correct guess")
    if lives > 0:
        print("You have", lives, "lives left")
    else:
        print("You ran out of lives :(")
        print("The word was", repr(phrase))
    return lives


retry = "y"
while retry not in ["n", "no"]:
    # Setting up variables
    guesses = []
    lives = 10
    print("Welcome to Hangman v1.0")

    # Running hangman game
    phrase = getphrase()
    print("Phrase accepted.")

    while lives > 0:
        print()
        print(get_guessed_phrase(guesses, phrase))
        input_guess()
        lives = check_lives(lives)

        if get_guessed_phrase(guesses, phrase) == phrase:
            print("The word was", repr(phrase), "You have won!")
            break

    retry = input("Do you want to play again? y/n ")

print("Thank you for playing.")
