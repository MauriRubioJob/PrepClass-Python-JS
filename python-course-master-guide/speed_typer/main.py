import random
from time import perf_counter

from pylev import levenshtein


def read_sentences(filename):
    with open(filename, "r") as file:
        sentences = file.read().splitlines()
    return sentences


def filter_sentences(sentences, min_length, max_length):
    filtered = []
    for sentence in sentences:
        length = len(sentence)
        if min_length <= length <= max_length:
            filtered.append(sentence)
    return filtered


def get_user_attempt():
    start_time = perf_counter()
    user_input = input()
    end_time = perf_counter()

    time_taken = end_time - start_time
    return user_input, time_taken


def calculate_speed(user_input, time_taken):
    chars_per_second = len(user_input) / time_taken
    chars_per_minute = chars_per_second * 60
    return chars_per_minute


def calculate_accuracy(original, user):
    num_of_changes = levenshtein(original, user)
    error_percent = num_of_changes / len(original)
    accuracy_percent = 1 - error_percent

    return accuracy_percent


sentences = read_sentences("sentences.txt")
sentences = filter_sentences(sentences, min_length=40, max_length=80)

sentence = random.choice(sentences)

print("Your sentence is:\n")
print(sentence)

input("\nPress Enter to start the timer and begin typing...")

user_input, time_taken = get_user_attempt()
speed = calculate_speed(user_input, time_taken)
accuracy = calculate_accuracy(sentence, user_input)

print("You typed at {} cpm with an accuracy of {}%".format(
    round(speed, 1), round(accuracy * 100, 1)))
