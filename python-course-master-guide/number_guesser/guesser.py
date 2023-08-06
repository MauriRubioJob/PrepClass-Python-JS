from random import randint, choice


print("Welcome to the NumberGuesser5000.")
print("Picking random number...")

# numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = range(1, 11)
number = choice(numbers)

while True:
    guess = int(input("Enter your guess: "))
    print("You guessed", guess)

    if number == guess:
        print("Well done, correct!")
        break
    if guess < number:
        print("Sorry, you're wrong. That was too low.")
    if guess > number:
        print("Sorry, you're wrong. That was too high.")


print("Program finished.")
