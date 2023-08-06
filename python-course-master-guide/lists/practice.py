
print("""Write a Python program to calculate the total of all
the items in a list using a for loop.""")

numbers = [91, 156, 98, 79, 62, 44, 164, 73, 7]


total = 0
for i in range(len(numbers)):
    n = numbers[i]
    total = total + n

print(total)


# total = sum(numbers)
# print(total)


################################################################################


print("""Write a Python program to find the largest number in a
list and print it out on the screen.""")

numbers = [250, 506, 406, 795, 314, 653, 382, 195, 427,
           676, 359, 511, 722, 605, 180, 948, 210, 96, 266, 53]


largest = 0
for i in range(len(numbers)):
    n = numbers[i]
    if n > largest:
        largest = n

print(largest)


# largest = max(numbers)
# print(largest)


################################################################################


print("""Write a Python program to count how many times a number
appears in a given list.""")

numbers = [2, 1, 34, 4, 4, 5, 6, 43, 45, 2, 24, 3, 4, 4, 324, 53, 4]
looking_for = int(input())


amount = 0
for i in range(len(numbers)):
    n = numbers[i]
    if n == looking_for:
        amount = amount + 1

print(amount)


amount = numbers.count(looking_for)
print(amount)


################################################################################


print("""Write a Python program to count the number of strings
that have a length of at least 2.""")

words = ["abc", "x", "y", "z", "hello", "wo", "rld", "123"]


################################################################################


print("""Write a program to separate odd and even numbers into
separate lists.""")

numbers = [16, 9, 21, 43, 18, 6, 1, 30]
odds = []
evens = []

input()
