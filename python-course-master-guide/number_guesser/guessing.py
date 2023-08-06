print("Welcome to the NumberGame5000.")
print("Pick a number between 1 and 100.")
print("After each guess, reply with 'too low' or 'too high' or 'correct'.")
input("Press Enter to start... ")

minimum = 1
maximum = 100

while True:
    guess = int((maximum - minimum) / 2 + minimum)
    print("My guess is", guess)

    feedback = input("Was that too low or too high?: ")

    if feedback == "correct":
        print("Yay I'm the best!")
        break
    if feedback == "too low":
        print("Okay. Changing minimum.")
        minimum = guess
    if feedback == "too high":
        print("Okay. Changing maximum.")
        maximum = guess
