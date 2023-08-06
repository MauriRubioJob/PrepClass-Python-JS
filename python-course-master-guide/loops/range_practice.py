
print("Print the letter X, 10 times.")
for counter in range(10):
    print("X")


################################################################################


print("Print the numbers 0 to 9.")
for counter in range(10):
    print(counter)


################################################################################


print("Print the numbers 1 to 10.")
for counter in range(1, 11):
    print(counter)


################################################################################


print("Print the numbers 0 to 9, in decreasing order.")
for counter in range(9, -1, -1):
    print(counter)


################################################################################


print("Print the numbers 1 to 10, in decreasing order.")
for counter in range(10, 0, -1):
    print(counter)


################################################################################


print("Print the even numbers from 2 to 10.")
for counter in range(2, 11, 2):
    print(counter)


################################################################################


print("Print the odd numbers from 1 to 9.")
for counter in range(1, 10, 2):
    print(counter)


################################################################################


print("Print the numbers 1 to 10. Print each number 5 times.")
for counter in range(1, 11):
    for counter2 in range(5):
        print(counter)


################################################################################


print("Print the numbers 1 to 10. Print each number itself number of times.")
for i in range(1, 11):
    for j in range(i):
        print(i)


################################################################################


print("Print the letter X, on 10 lines. Once on line 1, twice on line 2, three times on line 3, etc.")
for i in range(10):
    for j in range(i):
        print(5, end="")
    print()


################################################################################


print("Print the letter X, on 10 lines, same as previously. But fill in the empty space with the character \"-\".")
for i in range(1, 11):
    for j in range(i):
        print("X", end="")
    for j in range(10 - i, 0, -1):
        print("-", end="")
    print()
